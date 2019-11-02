
# Tree Review

TODO 1: Put this section after Graph Secion

TODO 2: 
Summarize this: 
https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

TODO 3:
Review Algorithm: 
Recursion version + Iterative version for pre-order, in-order, post-order traversal, (Leetcode 545) 
Order-level traversal (Leetcode 102, 199)

TODO 4:
Review QuickSort, QuickSelect(Leetcode 215), MergeSort

TODO 5:
Review PriorityQueue add and remove algorithm

TODO 6:
Review how to implement a HashMap: Hash Function + Address Conflict Resolution

TODO 7:
Understand Parser/Lexer etc (LeetCode 640, 536, PythonInterpreter)

# Graph Review 
Four major types of graph
Representation of the graph and the processing of the graph should be separated

* Graph - Undirected Unweighted 
  * DFS - Connectivity 
    * DFS Path - Single Source Path
    * CC - Connected Components
    * Cycle Detection - acyclic
    * Two Colorability - bipartite
  * BFS - Shortest
    * BFS Path - Single Source Shortest Path
  * SymbolGraph
* DiGraph - Directed Unweighted
  * DirectedDFS 
  * Topological Sort - Reverse Post DFS Order on a DAG
    * DirectedCycle
    * DepthFirstOrder
  * Strong Connected Digragh - Kosaraju's SCC - DFS of DG in reverse post order of the DG reverse
  * All Pair Reachability - TransitiveClosure - Run DirectedDFS on all vertex
* EdgeWeightedGraph - Undirected Weighted
  * Minimum Spanning Trees
    * Prim's algorithm: keep one connected piece, till all nodes reached
    * Kruskal's algorithm: keep adding small edges, till all nodes reached
* EdgeWeightedDigraph - Directed Digraph
  * Shortest Path
    * Dijkstra's algorithm: inviting the closest person among all club members into the club
  * General Shortest Path Algorithm
    * Bellman-Ford
  * Network Flow
    * Ford Fulkerson shortest-augmenting path maxflow algorithm

## Graph - Undirected Unweighted

### Representation
```java
public class Graph {
    private final int V;        //number of vertices, note the final
    private int E;              //number of edges
    private Bag<Integer>[] adj; //adjacency lists
    
    public Graph(int V) {
        this.V = V; this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++) {
            adj[v] = new Bag<Integer>();
        }
    }
    
    public Graph(In in) {
        this(in.readInt());     //Read V and construct this graph
        int E = in.readInt();   //Read E
        for (int i = 0; i < E; i++) {
            int v = in.readInt();   //Read one vertex
            int w = in.readInt();   //Read another vertex
            addEdge(v, w);          //Add edge connecting them
        }
    }
    
    public int V() { return V;}
    public int E() { return E;}
    
    public void addEdge(int v, int w) {
        adj[v].add(w);          //Add w to v's adjacency list
        adj[w].add(v);          //Add v to w's adjacency list
        E++;                    //Update Edge count
    }
    
    public Iterable<Integer> adj(int v) {
        return adj[v];
    }
}
```

### DFS

DFS is mainly used to check connectivity

* To search a graph, invoke a recursive method that visits vertices
* To visit a vertex
  * Mark it as having been visited
  * Visit (recursively) all the vertices that are adjacent to it **and that have not yet been marked**
    
```java
public class DepthFirstSearch {
    private boolean[] marked;
    private int count;
    
    public DepthFirstSearch(Graph G, int s) {
        marked = new boolean[G.V()];
        dfs(G, s);
    }
    
    private void dfs(Graph G, int v) {
        marked[v] = true;
        count++;
        for (int w: G.adj(v)) {
            if (!marked[w]) {
                dfs(w);
            }
        }
    } 
    
    public boolean marked(int w) {
        return marked[w];
    }
    
    public int count() {
        return count;
    }
}
```

#### DFS Path
```java
public class DepthFirstPaths {
    private boolean[] marked;   //Has dfs been called for this vertex
    private int[] edgeTo;       //Last known vertext reaching this vertex
    private final int s;        //Source vertex
    
    public DepthFirstPaths(Graph G, int s) {
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        this.s = s;
        dfs(G, s);
    }
    
    private dfs(Graph G, int s) {
        marked[s] = true;
        for (int w: G.adj(v)) {
            if (!marked[w]) {
                edgeTo[w] = v;      //Only difference from standard dfs
                dfs(G, w);
            }
        }
    }
    
    public boolean hasPathTo(int v) {
        return marked[v];
    }
    
    public Iterable<Integer> pathTo(int v) {
        if (!hasPathTo(v)) return null;
        Stack<Integer> path = new Stack<Integer>();
        for (int x = v; x != s; x = edgeTo[x]) {
            path.push(x);
        }
        path.push(s);
        return path;
    }
}
```

#### Connectd Components
Find the connected components of a graph.
a.k.a: Divide vertices into equivalence class

```java
public class CC {
    private boolean[] marked;
    private int[] id;
    private int count;
    
    public CC(Graph G) {
        marked = new boolean[G.V()];
        id = new id[G.V()];
        for (int s = 0; s < G.V(); s++) {
            if (!marked[s]) {
                dfs(G, s);
                count++;
            }
        }
    }
    
    private void dfs(Graph G, int v) {
        marked[v] = true;
        id[v] = count;
        for (int w: G.adg(v)) {
            if (!marked(w)) {
                dfs(G, w);
            }
        }
    }
    
    public boolean connected(int v, int w) {
        return id[v] == id[w];
    }
    
    public int id(int v) {
        return id[v];
    }
    
    public int count() {
        return count;
    }
}
```

#### Cycle
Is G acyclic? (assumes no self-loops or parallel edges) 

```java
public class Cycle {
    private boolean[] marked;
    private boolean hasCycle;
    
    public Cylce(Graph G) {
        marked = new boolean[G.V()];
        hasCycle = false;
        for (int s = 0; s < G.V(); s++) {
            if (!marked[s]) {
                dfs(G, s, s);
            }
        }
    }
    
    //v is the vertext to run dfs on
    //u is the source vertext leading to v
    private void dfs(Graph G, int v, int u) {
        marked[v] = true;
        for (int w: G.adj(v)) {
            if (!marked[w]) {
                dfs(G, w, v);
            } else if (w != u) {
                hasCycle = true; 
            }
        }
    }
}
```

#### Two-Colorability
Is G bi-partite? 
Can the vertices of a given graph be assigned in such a way that no edge connects vertices of the same color?

```java
public class TwoColor {
    private boolean[] marked;
    private boolean[] color;
    private boolean isTwoColorable = true;
    
    public TwoColor(Graph G) {
        marked = new boolean[G.V()];
        color = new boolean[G.V()];
        for (int s = 0; s < G.V(); s++) {
            if (!marked[s]) {
                dfs(G, s);
            }
        }
    }
    
    private void dfs(Graph G, int v) {
        marked[v] = true;
        for (int w: G.adj(v)) {
            if (!marked[w]) {
                color[w] = !color[v];
                dfs(G, w);
            } else if (color[w] == color[v]){
                isTwoColorable = false;
            }
        }
    }
    
    public boolean isBipartite() {
        return isTwoColorable;
    }
}
```

### BFS
* **Idea** 
    Maitainig a queue of all vertices that are *marked* but whose *adjacency lists haven not been checked*
        => Mark first, then put in the queue
* **Algorithm**
  * Put the source vertext on the queue, then perform the following step until queue is empty
    * Take the next vertext v from teh queue and mark it
    * Put onto the queue all unmarked vertices that are adjacent to v

#### BFS Path - Single Source Shortest Path

```java
public class BreathFirstPaths {
    private boolean[] marked;    //Is a **shortest** path to this vertext known
    private int[] edgeTo;
    private final int s;
    
    public BreathFirstPaths(Graph G, int s) {
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        this.s = s;
        bfs(G, s);
    }
    
    private void bfs(Graph G, int s) {
        Queue<Integer> queue = new Queue<>();
        marked[s] = true;
        queue.enqueue(s);
        while (!queue.isEmpty()) {
            int v = queue.dequeue();
            for (int w: G.adj(v)) {
                if (!marked[w]) {
                    edgeTo[w] = v;
                    marked[w] = true;
                    queue.enqueue(w);
                }
            }
        }
    }
    
    public boolean hasPathTo(int v) {
        return marked[v];
    }
    
    public Iterable<Integer> pathTo(int v) {
        //Same as DFS Path
    }
}
```

### SymbolGraph

```java
public class SymbolGraph {
    private Map<String, Integer> indexLookup;   //String -> Index
    private String[] nameLookup;              //Index -> String
    private Graph G;
    
    public SymbolGraph(String stream, String delimiter) {
        indexLookup = new HashMap<String, Integer>();
        In in = new In(stream);
        //--First Pass--
        //Builds index by reading strings to associate each distinct string with an index
        while(in.hasNextLine()) {
            String[] words = in.readLine().split(delimiter);
            for (int i = 0; i < word.length; i++) {
                if (!indexLookup.contains[a[i]]) {
                    indexLookup(words[i], indexLookup.size());
                }
            }
        }
        //Builds inverted index
        nameLookup = new String[indexLookup.size()];
        for (String name: indexLookup.keys()) {
            nameLookup[indexLookup.get(name)] = name;
        } 
        
        //--Second Path--
        //Builds the graph by connecting the first vertex on each line to all the others
        G = new Graph(indexLookup.size()) 
        in = new In(stream);
        while (in.hasNextLine()) {
            String[] words = in.readLine().split(delimiter);
            int v = st.get(words[0]);
            for (int i = 1; i < words.length; i++) {
                G.addEdge(v, indexLookup.get(words[i]));
            }
        }
    }
    
    public boolean contains(String s)   { return indexLookup.containsKey(s); }
    public int index(String s)          { return indexLookup.get(s); }
    public String name(int v)           { return nameLookup[v]; }
    public Graph G()                    { return G; }
}
```

You can construct a SymbolGraph from a data source (say dictionary: word will be vertices, and character difference by one will be edges), then run regular Graph algorithm on the return result of SymbolGraph.G(). For example: Word Ladder

### LeetCode Examples
#### DFS
##### [200 Number of Islands](https://leetcode.com/problems/number-of-islands)
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
11110
11010
11000
00000
```
Answer: 1

Example 2:
```
11000
11000
00100
00011
```
Answer: 3

```java
public class Solution {
    private int N;
    private int M;
    
    public int numIslands(char[][]grid) {
        int count = 0;
        N = grid.length;
        if (N == 0) return 0;
        M = grid[0].length;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == '1') {
                    DFSMarking(grid, i, j);
                    ++count;
                }
            }
        }
        return count;
    }
    
    private void DFSMarking(char[][] grid, int i, int j) {
        if (i < 0 || i >= N || j < 0 || j >= M || grid[i][j] != '1') return;
        grid[i][j] = '0';
        DFSMarking(grid, i-1, j); //Up
        DFSMarking(grid, i+1, j); //Down
        DFSMarking(grid, i, j-1); //Left
        DFSMarking(grid, i, j+1); //Right
    }
}
```
#### BFS
##### [127 WordLadder](https://leetcode.com/problems/word-ladder/) 
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.

```java
public class Solution {
    private class Graph {
        final private int V;
        private int E;
        private LinkedList<Integer>[] adj;
        
        public Graph(int V) {
            this.V = V;
            this.E = 0;
            adj = new LinkedList[V];
            for (int v = 0; v < V; v++) {
                adj[v] = new LinkedList<>();
            }
        }
        
        public int V() {return V;}
        public int E() {return E;}
        public List<Integer> adj(int v) {return adj[v];}
        public void addEdge(int v, int w) {
            adj[v].add(w);
            adj[w].add(v);
            E++;
        }
    }
    
    private boolean isNeighbor(String word1, String word2) {
        if (word1.length() !=  word2.length()) return false;
        
        int diff = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        return diff == 1;
    }
    
    private class SymbolGraph {
        private Graph G;
        private HashMap<String, Integer> st; //symbol -> index
        private String[] keys;
        
        public SymbolGraph(List<String> wordList) {
            st = new HashMap<>();
            for (String word: wordList) {
                if (!st.containsKey(word)) {
                    st.put(word, st.size());
                }
            }
            
            keys = new String[st.size()];
            for (String key: st.keySet()) {
                keys[st.get(key)] = key;
            }
            
            G = new Graph(st.size());
            for (int i = 0; i < st.size(); i++) {
                String word1 =  wordList.get(i);
                for (int j = i+1; j < st.size(); j++) {
                    String word2 = wordList.get(j);
                    if (isNeighbor(word1, word2)) {
                        G.addEdge(st.get(word1), st.get(word2));
                    }
                }
            }
        }
        
        public Graph G() {return G;}
        public int getIndex(String s) {return st.get(s);}
        public String getKey(int k) {return keys[k];}
    }
    
    private class BFPath {
        private boolean[] marked;
        private int[] edgeTo;
        private final int s;
        
        public BFPath(Graph G, int s) {
            marked = new boolean[G.V()];
            edgeTo = new int[G.V()];
            this.s = s;
            
            LinkedList<Integer> queue = new LinkedList<>();
            queue.addLast(s);
            while (!queue.isEmpty()) {
                int v = queue.removeFirst();
                marked[v] = true;
                for (int w: G.adj(v)) {
                    if (!marked[w]) {
                        edgeTo[w] = v;
                        marked[w] = true;
                        queue.addLast(w);
                    }
                }
            }
        }
        
        public boolean hasPathTo(int w) {
            return marked[w];
        }
        
        public int pathLength(int w) {
            if (!hasPathTo(w)) return 0;
            int count = 0;
            for (int v = w; v != s; v = edgeTo[v]) {
                count++;
            }
            return count+1;
        }
        
        public List<Integer> path(int w) {
            List<Integer> path = new LinkedList<>();
            if (!hasPathTo(w)) return path;
            for (int v = w; v != s; v = edgeTo[v]) {
                path.add(v);
            }
            path.add(s);
            return path;
        }
        
    }
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return 0;
        if (!wordList.contains(beginWord)) wordList.add(beginWord);
        SymbolGraph sg = new SymbolGraph(wordList);
        BFPath path = new BFPath(sg.G(), sg.getIndex(beginWord));
        
        List<Integer> aPath = path.path(sg.getIndex(endWord));
        
        /*LinkedList<String> transform = new LinkedList<>();
        for (int index: aPath) {
            transform.addFirst(sg.getKey(index));
        }
        System.out.println(transform);
        */
        return path.pathLength(sg.getIndex(endWord));
    }
}
```

##### 126 Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
  
Note:
* Return an empty list if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.

```java
public class Solution {
    private class Graph {
        final private int V;
        private int E;
        private List<Integer>[] adj;
        
        public Graph(int V) {
            this.V = V;
            this.E = 0;
            adj = new LinkedList[this.V];
            for (int v=0; v < V; v++) {
                adj[v] = new LinkedList<>(); 
            }
        }
        
        public int V() {return V;}
        public int E() {return E;}
        public void addEdge(int v, int w) {
            adj[v].add(w);
            adj[w].add(v);
            E++;
        } 
        public Iterable<Integer> adj(int v) {
            return adj[v];
        }
    }
    
    private boolean isNeighbor(String a, String b) {
        if (a.length() != b.length() ) {
            return false;
        }
        
        int diff = 0;
        for (int i = 0; i < a.length(); i++ ) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
            }
            
            if (diff > 1) {
                return false;
            }
        }
        
        return diff == 1;
    }
    
    public class SymbolGraph {
        private Map<String, Integer> st; //String -> index
        private String[] keys; //index -> String
        private Graph G;
        
        public SymbolGraph(List<String> wordList) {
            st = new HashMap<String, Integer>();
            for (String s: wordList) {
                if (!st.containsKey(s)) {
                    st.put(s, st.size());
                }
            }
            
            keys = new String[st.size()];
            for (String name: st.keySet()) {
                keys[st.get(name)] = name;
            }
            
            G = new Graph(st.size());
            for (int i = 0; i < wordList.size(); i++) {
                String s = wordList.get(i);
                for (int j = i+1; j < wordList.size(); j++) {
                    String s2 = wordList.get(j);
                    if (isNeighbor(s, s2)) {
                        G.addEdge(st.get(s), st.get(s2));
                    }
                }
            }
        }
        
        public Graph G() {return G;}
        public int getIndex(String s) {return st.get(s);}
        public String getString(int i) {return keys[i];}
    }
    
    public class DepthFirstAllPaths {
        private boolean[] onPath; //vertices is on current path;
        private LinkedList<Integer> path; //current path as a stack;
        private List<List<Integer>> paths;
        
        public DepthFirstAllPaths(Graph G, int s, int t) {
            onPath = new boolean[G.V()];
            path = new LinkedList<>();
            paths = new LinkedList<>();
            dfs(G, s, t);
        }
        
        private void dfs(Graph G, int v, int t) {
            path.addFirst(v);
            onPath[v] = true;
            if (v == t) {
                addTo(paths, path); //add a new path to current paths;
            } else {
                for (int w: G.adj(v)) {
                    if (!onPath[w])
                        dfs(G, w, t);
                }
            }
            path.removeFirst();
            onPath[v] = false;
        }
        
        private void addTo(List<List<Integer>>paths, List<Integer> path) {
            LinkedList<Integer> snapshot = new LinkedList<Integer>();
            for (int v: path) {
                snapshot.addFirst(v);
            }
            
            paths.add(snapshot);
        }
        
        public List<List<Integer>> getPaths() {
            return paths;
        }
        
        public boolean hasPaths() {
            return paths.size() != 0;
        }
        
    }
    
    
    
    public class BreadthFirstPaths {
        private boolean[] onPath;
        private LinkedList<Integer> path;
        private List<List<Integer>> paths;
        
        public BreadthFirstPaths(Graph G, int s, int t) {
            onPath = new boolean[G.V()];
            path = new LinkedList<Integer>();
            paths = new LinkedList<>();
            
            bfs(G, s, t);
        }
        
        private LinkedList<Integer> copyAndAppend(LinkedList<Integer> path, int vertex) {
            LinkedList<Integer> newPath = new LinkedList<Integer>();
            for (int v: path) {
                newPath.add(v);
            }
            newPath.add(vertex);
            return newPath;
        }
        
        private void bfs(Graph G, int s, int t) {
            LinkedList<LinkedList<Integer>> queue = new LinkedList<>();
            LinkedList<Integer>tempPath = new LinkedList<>();
            int minLegitPath = G.V();
            tempPath.add(s);
            
            queue.add(tempPath);
            while (!queue.isEmpty()) {
                LinkedList<Integer> aPath = queue.removeFirst();
                if (aPath.size() > minLegitPath) {
                    continue; //Cannot be minimum path
                } else {
                    boolean[] marked = new boolean[G.V()];
                    for (int v: aPath) {
                        marked[v] = true;
                    }
                    for (int v: G.adj(aPath.get(aPath.size()-1))) {
                        if (!marked[v]) {
                            LinkedList<Integer> newPath = copyAndAppend(aPath, v);
                            if (v == t) {
                                if (minLegitPath > newPath.size())
                                    minLegitPath = newPath.size();
                                addTo(paths, newPath);
                            } else {
                                queue.addLast(newPath);
                            }
                        }
                    }
                    
                }
                
            }
        }
        
        public void addTo(List<List<Integer>> paths, List<Integer> path) {
            LinkedList<Integer> snapshot = new LinkedList<>();
            for (int v: path) {
                snapshot.addLast(v);
            }
            paths.add(snapshot);
        }
        public boolean hasPaths() {
            return paths.size() != 0;
        }
        
        public List<List<Integer>> getPaths() {
            //prune out all duplicate and long paths
            Set<List<Integer>> solutions = new HashSet<>();
            int min = Integer.MAX_VALUE;
            for (List<Integer> path: paths) {
                if (path.size() < min) {
                    min = path.size();
                }
            }
            
            for (List<Integer> path: paths) {
                if (path.size() == min) {
                    solutions.add(path);
                }
            }
            
            return new ArrayList(solutions);
        }
    }
    
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> solutions = new ArrayList<>();
        
        if (!wordList.contains(endWord)) {
            return solutions;
        }
        
        wordList.add(beginWord);
        //wordList.add(endWord);
        SymbolGraph sg = new SymbolGraph(wordList);
        BreadthFirstPaths bfp = new BreadthFirstPaths(sg.G(), sg.getIndex(beginWord), sg.getIndex(endWord));
        //DepthFirstAllPaths dfps = new DepthFirstAllPaths(sg.G(), sg.getIndex(beginWord), sg.getIndex(endWord));
        
        
        if (!bfp.hasPaths()) {
            return solutions;
        }
        
        for (List<Integer> path: bfp.getPaths()) {
            //List<Integer> path = bfp.pathTo(sg.getIndex(endWord));
            List<String> solution = new ArrayList<>();
            for (int i = 0; i < path.size(); i++) {
                solution.add(sg.getString(path.get(i)));
            }
            solutions.add(solution);
        }
        
        return solutions;
    }
}
```

# LeetCode Summary

## Sliding Window

Here's a generic sliding window template that can solve most of substring problem. The idea is from [the awesome post here on leetcode](https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems)


### Template

I have adapted the original C++ code to java code as below

```java

int findSubstring(string s) {
	int[] map = new int[128];
	int begin = 0, end = 0; //two pointers for the begin and end of sliding window
	int counter; // check whether the substring is valid
	int d; //the length of substring
	
	for() {/*initialize the hash map here*/}
	
	while (end < s.size()) {
		if (map[s[end++]]-- ? ) {/*modify counter here*/}
		
		while (/*counter condition*/) {
			/*update d here if finding minimum*/
			//increase `begin` to make the window invalid/valid again
			if (map[s[begin++]]++ ?) {/*modify counter here*/}
		}
		
		/*update d here if finding maximum*/
	}
	return d;
}
```

Here is a reminder in the original post

***One thing needs to be mentioned is that when asked to find maximum substring, we should update maximum after the inner while loop to guarantee that the substring is valid. On the other hand, when asked to find minimum substring, we should update minimum inside the inner while loop.***

#### Template: Find max substring

```java
int findMinSubstring(string s) {
	int[] map = new int[128];
	int begin = 0, end = 0;
	int counter; //check whether the substring is valid
	int d; //the result of question regarding substring
	
	for() {/*initialize the hashmap here*/}
	
	while (end < s.size()) { //loop for moving end
		if (map[end++]-- ? ) {/*modify counter here*/}
		
		while (/*counter condition*/) { //loop for moving begin
			if (end - begin < d) d = end - (head = begin); 
			if (map[begin++]++ ? ) {/*modify counter here to make the substring invalid*/}
		}
	}
	return d;
}
```

#### Template: Find min substring
```java
int findMaxSubstring(string s) {
	int[] map = new int[128];
	int begin = 0, end = 0;
	int diff; //check whether the substring is valid, the difference between window and target
	int d, head; //the length and the head of the substring
	
	for() {/*initialize the hashmap here*/}
	
	while (end < s.size()) {
		if (map[end++]-- ? ) {/*modify diff here*/}
		while (/*diff condition*/) {	
			if (map[begin++]++ ? ) {/*modify diff here to make the substring valid*/}
		}
		if (end - begin > d) d = end - (head = begin);
	}
	return d;
}
```

### Practice

#### 438. Find All Anagrams in a String
```java
public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] map = new int[128];
        for (char c: p.toCharArray()) {
            map[c]++;
        }
        
        int begin=0, end=0, diff=p.length();
        List<Integer> result = new LinkedList<Integer>();
        while(end < s.length()) {
			//move right everytime, if the character exists in p's hash, decrease the diff
			//current hash value >= 1 means the character exists in p
            if (map[s.charAt(end++)]-- >= 1) diff--;
            
			//when the diff is down to 0, means we found the right anagram
			//then add window's left to result list
            if (diff == 0) result.add(begin);
            
			//if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
			//++ to reset the hash because we kicked out the left
			//only increase the diff if the character is in p
			//the diff >= 0 indicate it was original in the hash, cuz it won't go below 0
            if (end - begin == p.length() && map[s.charAt(begin++)]++ >= 0) diff++;
        }
        return result;
    }
}
```

#### 3. Longest Substring without repeating characters 
```java
public int lengthOfLongestSubstring(String s) {
        int begin = 0, end = 0, head = 0, length = 0;
        int[] map = new int[128];
        int diff = 0;
        
        while (end < s.length()) {
            if (map[s.charAt(end++)]++ > 0) diff++;
            while (diff > 0) {
                if (map[s.charAt(begin++)]-- > 1) diff--;
            }
            if (end - begin > length) length = end - (head = begin);
        }
        return length;
    }
```
#### 159. Longest Substring with At Most Two Distinct Characters

```java
public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int[] map = new int[128];
        int begin = 0, end = 0;
        int count = 0; //count of distinct characters
        int d = 0;
        int head = 0;
        
        while (end < s.length()) {
            if (map[s.charAt(end++)]++ == 0) count++; //update counter
            while (count > 2) { //if not a valid window yet
                //reduce to make the window again
                if (map[s.charAt(begin++)]-- == 1) count--;
            }
            if (end - begin > d) d = end - (head = begin);
        }
        return d;
    }
}
```

#### 904. [Fruit into Basket](https://leetcode.com/problems/fruit-into-baskets/) [Same as 159]
```java
class Solution {
    public int totalFruit(int[] tree) {
        int[] seenTimes = new int[tree.length]; //How many times you have seen a fruit type
        int begin = 0, end = 0;
        int fruitTypes = 0;         //This is the counter
        int currentMaxLength = 0;   //This is the d
        
        while (end < tree.length) {
            //Step 1: Slide window End to invalidate the window 
            // [Update map first, then use map, move END]
            //Update the interanltracker
            seenTimes[tree[end]]++;
            //First time seeing a new fruit
            if (seenTimes[tree[end]] == 1) {
                //Add new fruitTypes
                fruitTypes++;
            }
            //Move window END   
            end++;
            
            //Step 2: Make window valid by slide window left 
            // [Update map first, then use map, move BEGIN]
            //Remove seen fruits from beginning until we only got two fruit types
            while (fruitTypes > 2) {
                //Update internal tracker
                seenTimes[tree[begin]]--;
                //Last time seeing the fruit
                if (seenTimes[tree[begin]] == 0) {
                    //Remove seen fruit types
                    fruitTypes--;
                }
                //Move window BEGIN
                begin++;
            }
            
            //Step 3: Update the current maximum for valid window
            if (end - begin > currentMaxLength) {
                currentMaxLength = end - begin;
            }
        }
        return currentMaxLength;
    }
}
```

#### 76. Minimum Window Substring

```java
public class Solution {
    public void printState(int[] map) {
        for (int i='A'; i <='Z'; i++) {
            if (i == 'A' || i == 'B' || i == 'C' || i == 'D' || i == 'E' || i == 'O' || i == 'N')
            System.out.print((char)i + ": " + map[i] + ", ");
        }
        System.out.println();
    }
    
    public String minWindow(String s, String t) {
        int[] map = new int[128];
        for (int i = 0; i < t.length(); i++) map[t.charAt(i)]++;
        
        int begin = 0, end = 0;
        int d = Integer.MAX_VALUE, head = 0;
        int counter = t.length();
        
        while (end < s.length()) {
            System.out.println(s.substring(begin, end));
            System.out.println("begin:"+begin+", end:"+end+" counter:"+counter);
            printState(map);
            //update counter
            if (map[s.charAt(end)] > 0) counter--; 
            map[s.charAt(end)]--;
            end++;
            
            //a valid window is found find
            while (counter == 0) { 
                System.out.println("Valid found!");
                System.out.println(s.substring(begin, end));
                System.out.println("begin:"+begin+", end:"+end+" counter:"+counter);
                printState(map);
                if (end - begin < d) d = end - (head = begin); //update d with new minimum
                if (map[s.charAt(begin)] == 0) counter++; //update counter
                map[s.charAt(begin)]++;
                begin++;
            }
        }
        return (d == Integer.MAX_VALUE)?"":s.substring(head, head+d);
    }
}
```

## Backtrack

Here's a general approach to attack most of the [backtracking problems](https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning)

#### 78 Subset

```java
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> solutions = new LinkedList<>();
        Arrays.sort(nums);
        backtrack(solutions, new LinkedList<Integer>(), 0, nums);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> solution, int start, int[] nums) {
        solutions.add(new ArrayList<Integer>(solution));
        for (int i = start; i < nums.length; i++) {
            solution.add(nums[i]);
            backtrack(solutions, solution, i+1, nums);
            solution.remove(solution.size()-1);
        }
    }
}
```

#### 90 Subset II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = `[1,2,2]`, a solution is:
`
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
`

```java
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> solutions = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(solutions, new ArrayList<Integer>(), 0, nums);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> solution, int start, int[] nums) {
        solutions.add(new ArrayList<Integer>(solution));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            solution.add(nums[i]);
            backtrack(solutions, solution, i+1, nums);
            solution.remove(solution.size()-1);
        }
    }
}
```

#### 46 Permutation

```java
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> solutions = new ArrayList<>();
        //Arrays.sort(nums);
        backtrack(solutions, new ArrayList<Integer>(), nums);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int[] nums) {
        if (prefix.size()== nums.length) {
            solutions.add(new ArrayList<>(prefix));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (prefix.contains(nums[i])) continue;
                prefix.add(nums[i]);
                backtrack(solutions, prefix, nums);
                prefix.remove(prefix.size()-1);
            }
        }
    }
}
```

#### 47 Permutation II

```java
public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> solutions = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(solutions, new ArrayList<Integer>(), nums, new boolean[nums.length]);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int[] nums, boolean[] used) {
        if (prefix.size() == nums.length) {
            solutions.add(new ArrayList<Integer>(prefix));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] || i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;
                prefix.add(nums[i]); used[i] = true;
                backtrack(solutions, prefix, nums, used);
                prefix.remove(prefix.size() - 1); used[i] =  false;
            }
        }
    }
}
```

#### 51 NQueens 

```java
public class Solution {
    public List<List<String>> solveNQueens(int N) {
        List<List<Integer>> solutions = new ArrayList<>();
        backtrack(solutions, new ArrayList<Integer>(), N, 0);
        return format(solutions, N);
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int N, int row) {
        if (prefix.size() == N) {
            solutions.add(new ArrayList<Integer>(prefix));
        } else {
            boolean[] cannotPlace = new boolean[N];
            for (int rowA = 0; rowA < prefix.size(); rowA++) {
                //cannot place on same col
                int colA = prefix.get(rowA);
                cannotPlace[colA] = true; 
                //cannot place on diag  (col2 - col1)/(row2 - row1) = 1
                int colD = colA + row - rowA;
                if (colD >= 0 && colD < N) cannotPlace[colD] = true;
                //cannot place on reverse diag (col2 - col1)/(row2 - row1) = -1
                int colRD = colA + rowA - row;
                if (colRD >= 0 && colRD < N) cannotPlace[colRD] = true;
            }

            for (int i = 0; i < N; i++) {
                if (cannotPlace[i]) {
                    continue;
                } else {
                    prefix.add(i);
                    backtrack(solutions, prefix, N, row+1);
                    prefix.remove(prefix.size()-1);
                }
            }
        }
    }
    
    public List<List<String>> format(List<List<Integer>> solutions, int N) {
        List<List<String>> maps = new ArrayList<>();
        for (List<Integer> solution: solutions) {
            List<String> map = new ArrayList<>();
            for (int i = 0; i < solution.size(); i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < N; j++) {
                    if (j==solution.get(i)) sb.append('Q');
                    else sb.append('.');
                }
                map.add(sb.toString());
            }
            maps.add(map);
        }
        return maps;
    }
}
```

#### 52 NQueens II

```java
public class Solution {
    int solution;
    public int totalNQueens(int N) {
        solution = 0;
        backtrack(new ArrayList<Integer>(), N, 0);
        return solution;
    }
    
    public void backtrack(List<Integer> prefix, int N, int row) {
        if (prefix.size() == N) {
            solution++;
        } else {
            boolean[] cannotPlace = new boolean[N];
            for (int i = 0; i < prefix.size(); i++) {
                //cannot place on same col
                cannotPlace[prefix.get(i)] = true;
                //cannot place on diag
                int col = prefix.get(i) + i - row;
                if (col >= 0 && col < N) cannotPlace[col] = true;
                //cannot place on reverse diag
                col = prefix.get(i) + row - i;
                if (col >= 0 && col < N) cannotPlace[col] = true;
            }
            for (int i = 0; i < N; i++) {
                if (cannotPlace[i]) continue;
                prefix.add(i);
                backtrack(prefix, N, row+1);
                prefix.remove(prefix.size()-1);
            }
        }
    }
}
```

#### 39 Combination Sum

```java
public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> solutions = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(solutions, new ArrayList<Integer>(), 0, 0, candidates, target);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int sum, int start, int[] candidates, int target) {
        if (sum == target) {
            solutions.add(new ArrayList<>(prefix));
        } else {
            for (int i = start; i < candidates.length; i++) {
                if (sum + candidates[i] > target) return;
                else {
                    prefix.add(candidates[i]);
                    backtrack(solutions, prefix, sum + candidates[i], i, candidates, target);
                    prefix.remove(prefix.size()-1);
                }
            }
        }
    }
}
```

#### 40 Combinaiton Sum II

```
public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> solutions = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(solutions, new ArrayList<Integer>(), 0, 0, candidates, target);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int sum, int start, int[] candidates, int target) {
        if (sum == target) {
            solutions.add(new ArrayList<>(prefix));
        } else {
            for (int i = start; i < candidates.length; i++) {
                if (sum + candidates[i] > target) return;
                else if (i > start && candidates[i] == candidates[i-1]) continue;
                else {
                    prefix.add(candidates[i]);
                    backtrack(solutions, prefix, sum + candidates[i], i+1, candidates, target);
                    prefix.remove(prefix.size()-1);
                }
            }
        }
    }
}
```

#### 216 Combination Sum III
```java
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> solutions = new ArrayList<>();
        int[] candidates = new int[]{1,2,3,4,5,6,7,8,9};
        backtrack(solutions, new ArrayList<Integer>(), 0, 0, candidates, n, k);
        return solutions;
    }
    
    public void backtrack(List<List<Integer>> solutions, List<Integer> prefix, int sum, int start, int[] candidates, int target, int k) {
        if (prefix.size() > k || sum > target) {
            return;
        } else if (prefix.size() ==  k && sum == target) {
            solutions.add(new ArrayList<>(prefix));
        } else {
            for (int i = start; i < candidates.length; i++) {
                if (sum + candidates[i] > target) return;
                else if (i > start && candidates[i] == candidates[i-1]) continue;
                else {
                    prefix.add(candidates[i]);
                    backtrack(solutions, prefix, sum + candidates[i], i+1, candidates, target, k);
                    prefix.remove(prefix.size()-1);
                }
            }
        }
    }
}
```
