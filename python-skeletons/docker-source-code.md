#Docker Source Code Readthrough Notes

## Chapter 0: Setup

Fork the current docker repo
Clone the repo for your repository
Go to docker top directory and use `grep -nr '$SERARCH_STRING' . | less` to navigate through code base. [Note: -n: line number -r: recursively search in directory, . from current directory |:pipe to less, and from less use / to search further]

Interesting Packages used by Docker
[Cobra](https://github.com/spf13/cobra) : Cobra is both a library for creating powerful modern CLI applications as well as a program to generate applications and command files. It's used by `docker`, `etcd`, `Kubernetes` just to name a few

## Chapter 1: Docker Architecture

## Chapter 2. Docker Client CLI

1. Start with `docker/cmd/docker/docker.go`

Parse flag, and then create a new clientCli 
A cli object will encapsualte three handlers: `clientCli` for client, `newDaemonProxy` for daemon and `cobraAdaptor` for help messages

Then it will simply call c.Run() and pass in all the flags.
Run() will call command(), which will iterate through all handlers to handle the flag.
`Handler` is an interface that requires `Command` method
This is a **visitor pattern**, and a method `command` will be returned called as `command(args[1:]...)`

But things will essentially go to `cobraadaptor` in `docker/cli/cobraadaptor/adaptor.go`
Here's how it mux the command
Cobra is the struct below that implemented the `Handler` interface
```
type CobraAdaptor struct {
	rootCmd   *cobra.Command
	dockerCli *client.DockerCli
}
```
rootCmd has all the available commands registered during `NewCobraAdaptor()`
All of the commands registered has implemented `Handler` interface

Implementaton of `Handler` interface is to return one of command in its bag
```
func (c CobraAdaptor) Command(name string) func(...string) error {
	for _, cmd := range c.rootCmd.Commands() {
		if cmd.Name() == name {
			return func(args ...string) error {
				return c.run(name, args)
			}
		}
	}
	return nil
}
```
Note c.run() will initialize dockerCli and `setArgs()`, and calls `rootCmd.Execute`

2. How does `docker pull` command send request to daemon?

For example for `docker pull` command, at the end of day, cobra will get `NewPullCmd() *cobra.Command`, from `api/client/image/pull.go` and it calls `runPull()` with all the flags
`runPull()` will return the `ImagePullPrivileged()` that's defined in `api/client/trust.go`.
Underneath, `ImagePullPrivileged` will just encode authentication configuration and prepare `ImagePullOptions` and finally call `ImagePull`. 

`ImagePullOptions` is defined in  `docker/vendor/src/github.com/docker/engine-api/types/client.go` alongside other command options.
```
// ImagePullOptions holds information to pull images.
type ImagePullOptions struct {
	All           bool
	RegistryAuth  string // RegistryAuth is the base64 encoded credentials for the registry
	PrivilegeFunc RequestPrivilegeFunc
}
```

`ImagePull` is defined in `docker/vendor/src/github.com/docker/engine-api/client/image_pull.go` alongside with other commands
```
resp, err := cli.tryImageCreate(ctx, query, options.RegistryAuth)
```

`tryImageCreate` is defined in `./vendor/src/github.com/docker/engine-api/client/image_create.go` which will do the following REST call
```
func (cli *Client) tryImageCreate(ctx context.Context, query url.Values, registryAuth string) (*serverResponse, error) {
	headers := map[string][]string{"X-Registry-Auth": {registryAuth}}
	return cli.post(ctx, "/images/create", query, nil, headers)
}
```

The `post` method is defined in `./vendor/src/github.com/docker/engine-api/client/request.go`
```
// postWithContext sends an http request to the docker API using the method POST with a specific go context.
func (cli *Client) post(ctx context.Context, path string, query url.Values, obj interface{}, headers map[string][]string) (*serverResponse, error) {
	return cli.sendRequest(ctx, "POST", path, query, obj, headers)
}
```
`sendRequest` will call `sendClientRequest`, which will eventually construct the request head and body, and get the response back. These two functions are also defined in `./vendor/src/github.com/docker/engine-api/client/request.go`


The capacity of client is defined in `docker/vendor/src/github.com/docker/engine-api/client/interface.go` as an interface
```
type CommonAPIClient interface {
	ContainerAPIClient
	ImageAPIClient
	NodeAPIClient
	NetworkAPIClient
	ServiceAPIClient
	SwarmAPIClient
	SystemAPIClient
	VolumeAPIClient
	ClientVersion() string
	ServerVersion(ctx context.Context) (types.Version, error)
	UpdateClientVersion(v string)
}
```

And each interface client defines its own API set as an interface, such as for network subcommand, we have
```
type NetworkAPIClient interface {
	NetworkConnect(ctx context.Context, networkID, container string, config *network.EndpointSettings) error
	NetworkCreate(ctx context.Context, name string, options types.NetworkCreate) (types.NetworkCreateResponse, error)
	NetworkDisconnect(ctx context.Context, networkID, container string, force bool) error
	NetworkInspect(ctx context.Context, networkID string) (types.NetworkResource, error)
	NetworkInspectWithRaw(ctx context.Context, networkID string) (types.NetworkResource, []byte, error)
	NetworkList(ctx context.Context, options types.NetworkListOptions) ([]types.NetworkResource, error)
	NetworkRemove(ctx context.Context, networkID string) error
}
```


Note: 
Client will go through `docker/api/client/cli.go`
Server will be created through `docker/cmd/dockerd`

Random Note: ClientCli implemented `Handler` interface and registered `CmdExec` and `CmdInspect` in `api/client/commands.go`


TODO:
	Add a line by line walkthrough for `docker pull` based on the information provided above
	
## Chapter 3. Docker Daemon CLI

Docker daemon has three parts `server`, `engine` and `job`. `server` dispatches requests and redirects to `engine`, and `engine` will create `job` to handle the actual request

Let's see how the daemon got started from the command in the first place.

`docker daemon` or `service docker start`

1. Start with `docker/cmd/dockerd/docker.go`
Similiar to client, the docker daemon CLI starts in `docker/cmd/dockerd/docker.go`, it will start a `NewDaemonCli()`, parse the flag, and eventually call `initService` and `daemonCli.Start()`

The daemon struct is defined in `docker/cmd/dockerd/daemon.go`
```
type DaemonCli struct {
	*daemon.Config
	commonFlags *cliflags.CommonFlags
	configFile  *string

	api *apiserver.Server
	d   *daemon.Daemon
}
```

`daemon` field comes from `github.com/docker/docker/daemon`
`apiserver` field comes from `github.com/docker/docker/api/server`
Before diving into those two fields, let's see how to `start` and `stop` a `DamonCli`, eventually `Start()` in `docker/daemon/start` will be called

`daemonCli.start()` is defined in `docker/cmd/dockerd/daemon.go` as well, it will start the `apiserver` and `daemon` whereas NewDaemonCli will initilize `Config`, `commonFlags` and `configFile`. 

It will starts by register a `stopc` channel to listen for signal to terminate the daemon.
```
stopc := make(chan bool)
defer close(stopc)
...
signal.Trap(func() {
		cli.stop()
		<-stopc // wait for daemonCli.start() to return
	})
```

Then continue with loading the daemon CLI configuration files. It will create a Pidfile if doesn't exist already, then create `serverConfig` and `TLS` to finally initialize an apiserver.
```
serverConfig := &apiserver.Config{...}
api := apiserver.New(serverConfig)
cli.api = api
```

It will iterate through all the host and configure the communication stuff between daemons
```
for i := 0; i < len(cli.Config.Hosts); i++ {
		cli.Config.Hosts[i] opts.ParseHost(cli.Config.TLS, cli.Config.Hosts[i]); 
		api.Accept(protoAddrParts[1], ls...)
}
```

Registry service, containerd service and pluginInit will be created to finally initialize the Daemon
```
registryService := registry.NewService(cli.Config.ServiceOptions)
containerdRemote, err := libcontainerd.New(cli.getLibcontainerdRoot(), cli.getPlatformRemoteOptions()...)
pluginInit(cli.Config, containerdRemote, registryService)	
d, err := daemon.NewDaemon(cli.Config, registryService, containerdRemote)
```

A cluster will be created with this daemon, middleware will be created with api server, and router will be created with the cluster, daemon and the api server
```
c, err := cluster.New(cluster.Config{
		Root:    cli.Config.Root,
		Name:    name,
		Backend: d,
	})
cli.initMiddlewares(api, serverConfig)
initRouter(api, d, c)
```

The serve API routine never exits unless an error occurs, so start api server as a goroutine and wait on the error channel so that daemon doesn't exit
```
serveAPIWait := make(chan error)
go api.Wait(serveAPIWait)
```

Clean things up when an error shuts down api server, and docker daemon
```
c.Cleanup()
shutdownDaemon(d, 15)
containerdRemote.Cleanup()
```

Now let's move from the CLI and see how the daemon, api server got started on other side
Daemon creation will be explained in Chapter 4, API Server will be explained in Chapter 5






  


