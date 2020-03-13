# System Design Notes

* 程序 = 算法 + 数据结构
* 系统 = 服务 + 数据存储
* System Design = Logic Design + Infrastructure Design
* 系统设计 = 逻辑设计+ 架构设计

* 总结
  * 分布式系统
    * 分布式计算系统 MapReduce
    * 分布式存储系统 GFS
    * 分布式数据库系统 BigTable
  * 系统设计
    * Twitter/Facebook新鲜事系统 - Push vs Pull
    * 用户系统 - Memecache
    * TinyURL - 读多写少
    * Google爬虫&Typeahead - 写多读少
    * Uber位置系统 - Geohashing
    * 聊天系统&限速系统 

# Lecture 1 新鲜事系统 Introduction System Design & News Feed System - Push vs Pull
## Problem
[LINT 501 Mini Twitter](https://www.lintcode.com/problem/mini-twitter)	
[LC355 Design Twitter](https://leetcode.com/problems/design-twitter)

## 系统设计面试的两种形式 
* 设计某某系统 Design XXX System
  * 设计微博 Design Twitter
  * 设计人人 Design Facebook
  * 设计滴滴 Design Uber
  * 设计微信 Design Whatsapp
  * 设计点评 Design Yelp
  * 设计短网址系统 Design Tiny URL
  * 设计NoSQL数据库 Design NoSQL
* 找问题 Trouble Shouting
  * 网站挂了怎么办 What happened if we can not access a website
  * 网站太慢怎么办 What happened if a webserver is too slow
  * 流量增长怎么办 What should we do for increasing traffic

## 系统设计面试的评分标准
1. Working Solution 25%
2. Special Case 20%
3. Analysis 25%
4. Trade off 15%
5. Knowledge Base 15%

## 系统设计的4S分析法 - Scenario, Service, Storge, Scale
* Scenario: 询问设计哪些功能 10%
  * Ask, Features, Query Per Second, Daily Active User, Interfaces
* Service: 讲大系统拆为小系统 10%
  * Split into subtask, application, module
* Storage: 数据如何存储和访问 50%
  * Schema/Data/SQL/NoSQL/File System
* Scale: 解决缺陷, 处理可能遇到的问题 30%
  * Sharding/Optimize/Special Case

## Scenario - Ask & Analysis
* 需要设计哪些功能，设计得多牛
  * 1. Ask 问面试官
  * 2. Analysis 分析
* Ask Features
  * Step 1: List all twitter tasks
  * Step 2: Sort by priority
* Analysis: QPS - Queries Per Second
  * Read QPS: 300k
  * Write QPS: 5k
* 分析出 QPS 有什么用
  * QPS = 100: 用你的笔记本做 Web 服务器就好了
  * QPS = 1k: 
    * 用一台好点的 Web 服务器就差不多了
    * 需要考虑 Single Point Failure
  * QPS = 1m
    * 需要建设一个1000台 Web 服务器的集群
    * 需要考虑如何 Maintainance（某一台挂了怎么
* QPS和Web Server(服务器)/Database(数据库)之间的关系
  * 一台Web Server约承受量是 1k 的 QPS（考虑到逻辑处理时间以及数据库查询的瓶颈）
  * 一台 SQL Database 约承受量是 1k 的 QPS（如果 JOIN 和 INDEX query比较多的话，这个值会更小）
  * 一台 NoSQL Database (Cassandra) 约承受量是 10k 的 QPS
  * 一台 NoSQL Database (Memcached) 约承受量是 1M 的 QPS

## Service - Replay and Merge

## Storage
* Storage Types
  * 关系型数据库 SQL Database
    * 用户信息 User Table
  * 非关系型数据库 NoSQL Database
    * 推文 Tweets
    * 社交图谱 Social Graph (followers)
  * 文件系统 File System
    * 图片、视频 Media Files
  
### News Feed如何存取
* 什么是新鲜事 News Feed？
  * 你登陆 Facebook / Twitter / 朋友圈 之后看到的信息流
  * 你的所有朋友发的信息的集合
* 有哪些典型的新鲜事系统？
  * Facebook
  * Twitter
  * 朋友圈
  * RSS Reader
* 新鲜事系统的核心因素？
  * 关注与被关注
  * 每个人看到的新鲜事都是不同的

### Storage 存储 – Pull Model: Merge K Sorted Arrays - 主动撩妹
* 算法
  * 在用户查看News Feed时，获取每个好友的前100条Tweets，合并出前100条News Feed
  * K路归并算法 Merge K Sorted Arrays
* 复杂度分析 => 假如有N个关注对
  * News Feed => 则为N次DB Reads的时间 + K路归并时间(可忽略)
    * 为什么K路归并的时间可以忽略？因为在内存中做的
  * Post a tweet => 1次DB Write的时间
* 缺陷: 读的时候慢
  * N次DB Reads非常慢且发生在用户获得NewsFeed的请求过程中


```python
getNewsFeed(request)
    followings = DB.getFollowings(user=request.user)
    news_feed = empty
    for follow in followings:
        tweets = DB.getTweets(follow.to_user, 100)
        news_feed.merge(tweets)
    sort(news_feed)
    return news_feed

postTweet(request, tweet):
    DB.insertTweet(request.user, tweet)
    return success
```

### Storage 存储 – Push Model - 坐等被撩
* 算法
  * 为每个用户建一个List存储他的News Feed信息
  * 用户发一个Tweet之后，将该推文逐个推送到每个用户的News Feed List中
    * 关键词：Fanout
  * 用户需要查看News Feed时，只需要从该News Feed List中读取最新的100条即可
* 复杂度分析
  * News Feed => 1次DB Read
  * Post a tweet => N个粉丝，需要N次DB Writes
  * 好处是可以用异步任务在后台执行，无需用户等待
* 缺陷: 写的时候慢
  * 异步执行, 更新不及时
  * followers的数目可能很大
* 好处
  * Fanout可以用异步任务在后台执行，无需用户等待

```python
getNewsFeed(request)
    return DB.getNewsFeed(request.user)

postTweet(request, tweet_info)
    tweet = DB.insertTweet(request.user, tweet_info)AsyncService.fanoutTweet(request.user, tweet)
    return success

AsyncService::fanoutTweet(user, tweet)
    followers = DB.getFollowers(user)
    for follower in followers:
        DB.insertNewsFeed(tweet, follower
```

### Pull vs Push
* 热门Social App的模型
  * Facebook – Pull
  * Instagram – Push + Pull
  * Twitter – Pull
* 误区
  * 不坚定想法，摇摆不定
  * 不能表现出Tradeoff的能力
  * 无法解决特定的问题

## Scale
* 如何优化
  * 第一步 Step 1: Optimize
    * 解决设计缺陷 Solve Problems
      * Pull vs Push, Normalize vs De-normalize
    * 更多功能设计 More Features
      * Edit, Delete, Media, Ads
    * 一些特殊用例 Special Cases
      * Lady Gaga, Inactive Users
  * 第二步 Step 2: Maintenance
    * 鲁棒性 Robust
      * 如果有一台服务器/数据库挂了怎么办
    * 扩展性 Scalability
      * 如果有流量暴增，如何扩展
* 解决Pull的缺陷
  * 在 DB 访问之前加入Cache
  * Cache 每个用户的Timeline
    * N次DB请求 → N次Cache请求 (N是你关注的好友个数)
    * Trade off: Cache所有的？Cache最近的1000条？
  * Cache 每个用户的 News Feed
    * 没有Cache News Feed的用户：归并N个用户最近的100条Tweets，然后取出结果的前100条
    * 有Cache News Feed的用户༚归并N个用户的在某个时间戳之后的所有Tweets
* 解决Push的缺陷
  * 浪费更多的存储空间 Disk
    * 与Pull模型将News Feed存在内存(Memory)中相比
    * Push模型将News Feed存在硬盘(Disk)里完全不是个事儿
    * Disk is cheap
* 解决明星问题
  * 粉丝数目 followers >> 关注数目 followin
    * Lady Gaga问题
    * 无解？完全切换回Pull？
    * Trade off: Pull + Push vs Pull
  * Push 的挑战
    * Fanout 的过程可能需要几个小时！
  * 面试时错误的回答方案: 既然 Push 不行，那我们就切换到 Pull 吧！
  * 正确的思路
    * 尝试在现有的模型下做最小的改动来优化
    * 比如多加几台用于做 Push 任务的机器，Problem Solved!
    * 对长期的增长进行估计，并评估是否值得转换整个模型
  * Push 结合 Pull 的优化方案
    * 普通的用户仍然Push
    * 将Lady Gaga这类的用户, 标记为明星用户, 不Push到用户的News Feed中
    * 当用户需要的时候，来明星用户的Timeline里取，并合并到News Feed里
* Push vs Pull
  * Push | Pull
    -- | --
    资源少 | 资源充足
    想偷懒，少写代码 | 
    实时性要求不高 | 实时性要求高
    用户发帖比较少 | 用户发帖很多
    双向好友关系，没有明星问题（比如朋友圈） | 单向好友关系，有明星问题
  * 为什么既然大家都用Pull，我们仍然要学习Push？
    * 系统设计不是选择一个最好的方案, 而是选择一个最合适的方案
    * 如果你没有很大的流量，Push是最经济最省力的做法

# Lecture 2 用户系统 Design User System - Database & Memcache
## Problem
* Required
  * LINT 519: Consistent Hashing
  * LINT 538: Memcache
  * LINT 502:  Mini Cassandra
* Optional
  * LINT 24: LFU Cache
  * LINT 134: LRU Cache

## User System - 读多写少系统的4S分析(Scenario, Service, Storage, Scale)
* 特点:
  * 用户系统: 读多写少
  * 机器系统: 写多读少
* Scenario 场景 - 注册, 登录, 查询, 修改
  * Support 100 M Daily Active User
  *  注册, 登录, 修改 QPS
    *  100M * 0.1/ 86400 ~ 100 QPS
    *  Peak = 100 * 3 = 300
  *  查询
    *  100M * 100 /86400 ~ 100K
    *  100 = 平均用户每天的用户查询次数
    *  Peak = 100 * 3 = 300K
    *  => 300台MySQL or 一台1台memcached
* Service服务
  * AuthService: 登录注册
  * UserService: 用户信息的存储与操作
  * Friendship Service: 好友关系
* Storage储存
  * SQL数据库性能
    * e.g.: MySQL / PosgreSQL
    * 约 1k QPS 这个级别
  * 硬盘型NoSQL
    * e.g.: MongoDB / Cassandra
    * 约 10k QPS 这个级别
  * 内存型NoSQL数据库 - (不可断电,但效率高)
    * e.g.: Redis / Memcached
    * 100k ~ 1m QPS 这个级别
* Scale优化
  * 读多写少-利用Cache
  
### 内存型NoSQL常用软件 - Memcached vs Redis
* Cache:
  * 在速度有差异下即可使用的概念, 与存储介质无关
    * File System: 可以是网络的Cache
* Memcached
  * 不支持数据持久化
  * Cache-aside，用户自己去handle cache miss
  * 服务器分别与 DB 和 Cache 进行沟通 DB 和 Cache之间不直接沟通 
    * Memcached + MySQL
* Redis - 特别适合小型网址
  * 支持数据持久化
  * Cache-through
  * 服务器只和 Cache 沟通, Cache 负责 DB 去沟通，把数据持久化
    * 可以理解为 Redis 里包含了一个 Cache 和一个 DB

## UserService
```python
    class UserService:
        def getUser(self, user_id):
            key = "user::%s" % user_id
            user = cache.get(key)
            if user:
                return user
            user = database.get(user_id)
            cache.set(key, user)
            return user

        def setUser(self, user)
            key = "user::%s" % user_id
            cache.delete(key)
            databse.set(user)
```
* setUser的正确写法
  * A: database.set(user); cache.set(key, user); 
    * 脏数据: dataset set可能失败, 所以不能去set cache, 否则数据不一致
  * B: cache.set(key, user); database.set(user); 
    * 脏数据: dataset set可能失败, 所以不能去set cache, 否则数据不一致
  * C: cache.delete(key); database.set(user); 
    * 这种方式比较好, 哪怕database失败了, cache也可以去database重新读
    * 但是getUser和setUser之间可能有race condition
  * D: database.set(user); cache.delete(key);
    * 脏数据: dataset set可能失败, 所以不能去set cache, 否则数据不一致

## Authentication Service
### 如何实现登陆与保持登陆
* Session Table的fields

Fields | Type | Notes
--|--|
session_key | string | 一个 hash 值，全局唯一，无规律
user_id | Foreign key | 指向 User Table
expire_at | timestamp | 什么时候过期

* 用户 Login 以后
  * 创建一个 session 对象
  * 并把 session_key 作为 cookie 值返回给浏览器
  * 浏览器将该值记录在浏览器的 cookie 中
  * 用户每次向服务器发送的访问，都会自动带上该网站所有的 cookie
  * 此时服务器检测到cookie中的session_key是有效的，就认为用户登陆了
* Session Table存在哪儿
  * 一般来说, 都可以
  * 即便存在 Cache 里, 断电了相当于让所有用户都 logout 也没啥大不了 
  * 存在数据库里肯定更好, 特别是**大网站**, 以免断电后大量用户需要同时登陆

 ## User System小结
  * 写很少
    * 从QPS的角度来说，一台 MySQL 就可以搞定了 
  * 读很多
    * 可以使用 Memcached 进行读操作优化
  * 读写操作都很多，怎么办?
    * 方法一:使用更多的数据库服务器分摊流量
    * 方法二:使用像 Redis 这样的读写操作都很快的 Cache-through 型 Database
      * Memcached 是一个 Cache-aside 型的 Database，Client 需要自己负责管理 Cache-miss 时数据的 loading

## Friendship Service
* 单向好友(Twitter、Instagram、微博)
* 双向好友(WhatsApp、Facebook 、 微信)
  * 方案1:存为两条信息，A关注了B，B关注了A
  * 方案2:存为一条信息，但查询的时候需要查两次
* 好友关系所涉及的操作非常简单，基本都是 key-value:
  * 求某个 user 的所有关注对象
  * 求某个 user 的所有粉丝
  * A 关注 B => 插入一条数据
  * A 取关 B => 删除一条数据

### 选择标准: SQL vs NoSQL
* 原则1: 大部分的情况，用SQL也好，用NoSQL也好，都是可以的
* 原则2: 需要支持Transaction只能用SQL
* 原则3: SQL省事. NoSQL很多事儿都要亲力亲为(Serialization, Secondary Index)
* 原则4: NoSQL性能好. 硬盘型的NoSQL比SQL一般都要快10倍以上
  
### Cassandra: 硬盘型NoSQL分析
* Cassandra 是一个三层结构的 NoSQL 数据库
  * 第一层:row_key - 用于hash
    * 用来找数据在哪个机器
    * 任何的查询都需要带上这个key，无法进行range query
    * 最常用的row_key: user_id
  * 第二层:column_key - 用于sort
    * 是排序的，可以进行range query
    * 可以是复合值，比如是一个 timestamp + user_id 的组合
  * 第三层:value
    * 一般来说是 String
    * 如果你需要存很多的信息的话，你可以自己做 Serialization
      * Serialization: 把一个 object / hash 序列化为一个 string, 比如把一棵二叉树序列化
* Column: SQL vs NoSQL
  * SQL的column是在Schema中预先指定好的，不能随意添加
      * 一条数据一般以row为单位 => 取出整个row作为一条数据
  *  NoSQL的column是动态的，无限大，可以随意添加
     *  一条数据一般以 grid 为单位，row_key + column_key + value => 一条数据
     *  只需要提前定义好 column_key 本身的格式(是一个 int 还是一个 int+string)

## Scale
### Single Point Failure - 数据库挂了怎么办
* 万一这一台数据库挂了
  * 短暂的挂:网站就不可用了
  * 彻底的挂:数据就全丢了
* 所以你需要做两件事情
   * 1. Sharding 
   * 2. Replica
  
### Sharding 数据拆分 - 只有NoSQL有这个功能
* NoSQL vs SQL
  * SQL自身不带 Sharding 功能，需要码农亲自上手 
  * Cassandra为例的NoSQL大多数都自带 Sharding 
  * 这就是为什么程序员要发明 NoSQL 
* Types
  * Vertical Sharding 
  * Horizontal Sharding
  
#### Vertical Sharding - 不能解决Single Point Failure
* 普通用法
  * User Table 放一台数据库
  * Friendship Table 放一台数据库 
  * Message Table 放一台数据库
* 高级用法
  * email / username / password 不会经常变动
  * push_preference, avatar 相对来说变动频率更高
  * 可以把他们拆分为两个表 User Table 和 User Profile Table, 然后再分别放在两台机器上
  * 这样如果 UserProfile Table 挂了，就不影响 User 正常的登陆
* 缺点
  * 不能解决Single Point Failure

#### Horizontal Sharding - Scale核心考点
* 如何拆分 Friendship Table
  * 粗暴的想法
    * 我们有10台数据库的机器 于是想到按照 from_user_id % 10 进行拆分
  * 假如10台机器不够用怎么办
     * 我现在新买了1台机器, 原来的%10，就变成了%11
     * 位置大迁移 - 常见问题
       * 慢，牵一发动全身
       * 迁移期间，服务器压力增大，容易挂
       * 容易􏰀成数据的不一致性
  * Consistent Hashing - 如何解决位置大迁移问题
    * 将 key 模一个很大的数，比如 360
    * 将 360 分配给 n 台机器，每个机器负责一段区间
    * 区间分配信息记录为一张表存在 Web Server 上
    * 新加一台机器的时候，在表中选择一个位置插入，匀走相邻两台机器的一部分数据

### Replica 数据备份
* NoSQL Replica: 常用方法
  * 通常的做法是一式三份(重要的事情“写”三遍)
  * 顺时针找3台机器
  * Replica 同时还能分摊读请求
* SQL Replica: Master-Slave
  * 原理 Write Ahead Log
    * SQL 数据库的任何操作，都会以 Log 的形式做一份记录 • 比如数据A在B时刻从C改到了D
    * Slave 被激活后，告诉master我在了
    * Master每次有任何操作就通知 slave 来读log
    * 因此Slave上的数据是有“延迟”的
  * Master 挂了怎么办?
    * 将一台 Slave 升级 (promote) 为 Master，接受读+写 • 可能会造成一定程度的数据丢失和不一致

## User System总结 - SQL vs NoSQL
- | SQL | Disk NoSQL | Mem NoSQL
--|--|--|--
Example | MySQL | MongoDB / Cassandra | Redis / Memcached
QPS | 1k | 10k | 100k ~ 1m
Service | UserService| FriendshipService | AuthService <li>Session (存在服务器端)<li>Cookie(存在浏览器端)
Sharding | N/A | Consistent Hashing | Consistent Hashing 
Replica | Master/Slave | 存三份 | 存三份

* Single Point Failure
  * Sharding/Partition
    * Vertical Sharding
    * Horizontal Sharding -  Consistent Sharing
  * Replica

# Lecture 3 - 致性哈希算法与短网址系统 Consistent Hashing & Design Tiny Url
## Problem
* LINT Consistent Hashing II
* 
## Concept
* Consistent Hashing
  * 简单的Consistent Hashing方法的回顾及缺陷分析
  * 一个更优的 Consistent Hashing 方法
* Replia
  * SQL 通常如何进行备份
  * NoSQL 通常如何进行备份?
* 设计一个短网址系统 Design Tiny Url
  * 4S 分析法

## Consistent Hashing - Horizontal Sharding的秘密武器
* 不一致Hashing
  * `% n` 的方法是一种最简单的 Hash 算法
  * 但是这种方法在 n 变成 n+1 的时候，每个 `key % n`和 `% (n+1)` 结果基本上都不一样
  * 造成了75%的数据迁移
* 一个简单的一致性Hash算法
  * 算法
    * 将 key 模一个很大的数，比如 360 => 在圆上
      * n从2变化到3，只有1/3的数据移动
    * 将 360 分配给 n 台机器，每个机器负责一段区间
    * 区间分配信息记录为一张表存在 Web Server 上
    * 新加一台机器的时候，在表中选择一个位置插入(e.g.: 两个和最大), 匀走相邻**两台**机器的一部分数据
  * 缺陷
    * 缺陷1: 数据分布不均匀
    * 缺陷2: 迁移压力大
* Consistent Hashing - 更实用的方法
  * 这个环的大小从 0~359 变为 0~2^64-1
  * 引入 Micro shards / Virtual nodes 的概念
    * 一台实体机器对应 1000 个 Micro shards / Virtual nodes
  * 每新加入一台机器，就在环上随机撒 1000 个点作为 virtual nodes
  * 需要计算某个 key 所在服务器时
    * 计算该key的hash值——得到0~2^64-1的一个数，对应环上一个点 • 顺时针找到第一个virtual node
    * 该virtual node 所在机器就是该key所在的数据库服务器
  * 新加入一台机器做数据迁移时
    * 1000个virtual nodes 各自向**顺时针**的一个 virtual node 要数据
* 例子 
  * 加入说环上目前顺时针的情况分别是：
    * `1 -> 2 -> A -> 3 -> 4 -> B`
    * 那么此时 数据1 和2 是存在机器A的，数据3和4 是存在机器B的。
  * 然后此时新加入一个机器C。这个机器hash之后被分配在数据3和4之间。
    * `1->2->A->3->C->4->B`
    * 也就是说，在新的结构中，3需要存在机器C上，而3 原本是存在机器B上的，
    * 所以他要顺时针问B要数据。而不是逆时针问A要。
  * 新的服务器向**顺时针**的下一台服务器索取**逆时针**的一段区间内的数据
  
## Replica 数据备份
### Backup vs Replica
  * Backup
    * 一般是周期性的，比如每天晚上进行一次备份
    * 当数据丢失的时候，通常只能恢复到之前的某个时间点
    * Backup 不用作在线的数据服务，不分摊读
  * Replica
    * 是实时的， 在数据写入的时候，就会以复制品的形式存为多份
    * 当数据丢失的时候，可以马上通过其他的复制品恢复
    * Replica 用作在线的数据服务，分摊读
  * 既然 Replica 更牛，那么还需要 Backup么
    * 便宜

### MySQL Replica - Master/Slave
* 以MySQL为代表SQL型数据库，通常“自带” Master-Slave 的
Replica 方法
  * Master 负责写，
  * Slave 负责读 
  * Slave 从 Master 中同步数据
* 原理 Write Ahead Log
  * SQL 数据库的任何操作，都会以 Log 的形式做一份记录 • 比如数据A在B时刻从C改到了D
  * Slave 被激活后，告诉master我在了
  * Master每次有任何操作就通知 slave 来读log
  * 因此Slave上的数据是有“延迟”的
* Master 挂了怎么办?
  * 将一台 Slave 升级 (promote) 为 Master，接受读+写 
  * 可能会造成一定程度的数据丢失和不一致

## NoSQL Replica
* 以 Cassandra 为代表的 NoSQL 数据库 
  * 通常将数据“顺时针”存储在 Consistent hashing 环上的三个 virtual nodes 中
*  SQL“自带” 的 Replica 方式是 Master Slave, “手动” 的 Replica 方式也可以在 Consistent Hashing 环上顺时针存三份
*  NoSQL就是在 Sharding 和 Replica 上帮你偷懒用的

## Design Tiny URL - 短网址系统 - 30% System Design会面的题
### 回顾系统设计的常见误区 
* 错误假设
  * 流量一定巨大无比
  * 那必须是要用NoSQL了 
  * 那必须是分布式系统了
* 错误恢复
  * 某同学:先来个Load Balancer，后面一堆Web Server，然后 memcached，最底层NoSQL，搞定!

### 系统设计问题的基本步骤 - 4S 分析法

1. 提问:分析功能/需求/QPS/存储容量——Scenario 
2. 画图:根据分析结果设计“可行解”—— Service+Storage
3. 进化:研究可能遇到的问题，优化系统 —— Scale

### Scenario: 分析QPS+Storage
1. 询问面试官微博日活跃用户
  * 约100M
2. 推算产生一条Tiny URL的QPS
  * 假设每个用户平均每天发 0.1 条带 URL 的微博
  * Average Write QPS = 100M * 0.1 / 86400 ~ 100
  * Peak Write QPS = 100 * 2 = 200
3. 推算点击一条Tiny URL的QPS
  * 假设每个用户平均点1个Tiny URL
  * Average Read QPS = 100M * 1 / 86400 ~ 1k
  * Peak Read QPS = 2k
4. 推算每天产生的新的 URL 所占存储
   * 100M * 0.1 ~ 10M 条
   * 每一条 URL 长度平均 100 算，一共1G
   * 1T 的硬盘可以用 3 年
**结论**
  * 2k QPS: 一台 SSD支持 的MySQL完全可以搞定

## Service - 逻辑块聚类与接口设计
* TinyUrl只有一个UrlService
  * 本身就是一个小Application
  * 无需关心其他的
* 函数设计
  * UrlService.encode(long_url) 
  * UrlService.decode(short_url)
* 访问端口设计
  * GET /<short_url>
    * return a Http redirect response
  * POST /data/shorten/
    * Data = {url: http://xxxx }
    * Return short url



## Storage 数据存取
* 步骤
  * 第一步:Select 选存储结构 
  * 第二步:Schema 细化数据表

### SQL vs NoSQL
* Transaction Support
  * NoSQL不支持Transaction
* SQL Query?
  * NoSQL的SQL Query不是太丰富
  * 也有一些NoSQL的数据库提供简单的SQL Query支持
* 是否想偷懒?
  * 大多数 Web Framework 与 SQL 数据库兼容得很好
    * 用SQL比用NoSQL少写很多代码
  * SQL 需要码农自己写代码来 Scale - Sharding, Replica
  * NoSQL 这些都帮你做了
* Sequential ID?
  * SQL 为你提供了 auto-increment 的 Sequential ID, 也就是1,2,3,4,5 ...
  * NoSQL的ID并不是 Sequential 的
* Performance
  * NoSQL 的性能更高

### 算法
#### 方法1 - 随机生成ShortURL + 数据库去重
```java
public String longToShort(String url) {
    while(true) {
        String shortURL = randomShortURL();
        if (!database.filter(shortURL=shortURL).exists()) {
            database.creaste(shortURL=shortURL, longURL=url);
            return shortURL;
        }
    }
}
```

* 优点:实现简单
* 缺点:生成短网址的􏰁度随着短网址越来越多变得越来越慢

#### 方法2: 进制转换 Base62
* Base62
  * 将 6 位的short url看做一个62进制数(0-9, a-z, A-Z)
  * 每个short url 对应到一个整数
  * 该整数对应数据库表的Primary Key —— Sequential ID
* 为什么只用6位? 表示的不同 URL够用了
  * 5 位 = 625 = 0.9B = 9 亿
  * 6 位 = 626 = 57 B = 570 亿
  * 7 位 = 627 = 3.5 T = 35000 亿
* 优点:效率高
* 缺点:依赖于全局的自增ID
* 实现
  * 因为需要用到自增ID(Sequential ID)，因此只能选择使用 SQL 型数据库。
  * 表单结构如下，shortURL 可以不存储在表单里，因为可以根据 id 来进行换算

## Scale 进化
### 如何提速？
  * 利用缓存提速(Cache Aside)
    * 缓存里需要存两类数据:
      * long to short(生成新 short url 时需要)
      * short to long(查询 short url 时需要)
  * 利用地理位置信息提速
  * 优化服务器访问速度
    * 不同的地区，使用不同的 Web 服务器
    * 通过DNS解析不同地区的用户到不同的服务器
  * 优化数据访问速度
    * 使用Centralized MySQL+Distributed Memcached
    * 一个MySQL配多个Memcached，Memcached跨地区分布

### 如何扩展？
  * 解决“存不下”的问题 - Storage的角度
  * 解决“忙不过”的问题 - QPS的角度
  * Vertical Sharding 
    * 将多张数据表分别分配给多台机器
  * Horizontal Sharding
    * 用什么做Sharding Key?
      * 如果用 ID，如何查询 Long Url?
      * 如果用Long Url，如何查询 ID?
    * 预留一位作为sharding key

### Multi Region的进一步优化
* 按照网站的地域信息进行 Sharding
  * 中国的用户访问时，会被DNS分配中国的服务
  * 中国访问中国是主流需求，优化系统就是要优化主要的需求


### 如何自定义短连接
* 新建一张表存储自定义URL
  * CustomURLTable
* 查询长链接
  * 先查询CustomURLTable
  * 再查询URLTable
* 根据长链接创建普通短链接
  * 先查询CustomURLTable是否存在
  * 再在URLTable中查询和插入
* 创新自定义短链接
  * 查询是否已经在URLTable中存在
  * 再在CustomURLTable中查询和插入
* 错误的想法
  * 在URLTable中加一个column 
  * 大部分数据这一项都会是空

## 总结
* Scenario - 各种问面试官问题，搞清楚要干嘛
  * 场景分析:要做什么功能
  * 需求分析:QPS和Storage
  *  应用服务:UrlService
* Service + Storage - 根据问到的内容进行分析 得到一个基本可以work的方案
  * 数据分析:选SQL还是NoSQL
  *  数据分析:细化数据库表
  *  得到一个Work Solution
* Scale
  * 提高Web服务器与数据服务器之间的访问效率
    * 利用缓存提高读请求的效率
  * 提高用户与服务器之间的访问效率
    * 解决了中国用 户访问美国服 务器慢的 问题
  * 提高QPS，将数据分配到多台服务器
    * 解决流量继续增大一台数据库服务器无法满足的问题
  * 提高中国的Web服务器与美国的数据库服务器通信较慢的问题
    * 按照网站地域信息 进行Sharding 
  * 提供 Custom URL 的功能

# Lecture 4 分布式文件系统 GFS - Master/Slave
## 分布式系统
* 概述
  * 用多台机器去解决一台机器上不能够解决的问题
  * 存储/QPS
* 谷歌三剑客
  * Distributed File System (Google File System)
    * 怎么有效存储数据?
    * No SQL 底层需要一个文件系统
  * Map Reduce
    * 怎么快速处理数据?
  * Bigtable = No-SQL DataBase
    * 怎么连接底层存储和上层数据
## Scenario 场景分析
* 需求1
  * 用户写入一个文件， 用户读取一个文件. 
  * 支持多大的文件?
    * 越大越好?比如>1000T 
* 需求2
  * 多台机器存储这些文件 
  * 支持多少台机器?
    * 越多越好?10万台, Google 2007 year

## Service 服务 - Master/Slave
* Master Slave
  * Advantage
    * Simple Design
    * 数据很容易保持一致 
  * Disadvantage
    * Single Point of Failure

-|DB|GFS(HDFS)
--|--|--
Master | 存储数据 | 管理者(不存储数据)
Slave | BackUp | 被管理者(存储实际文件 ，partition关系)

* Peer to Peer
  * Advantage: High Availability
  * Disadvantage: Synchronization between peers

## Storage 存储

### One File in One Machine: 10MB
* Database vs Filesystem
  * 数据库是文件系统的特例，适用于**结构化**的信息
* Metadata
  * 描述“其他数据”而存储的信息 
  * Metadata 访问 常常多于 内容的访问
* 文件存储
  * Windows就是连续存储
    * Disadvantage: Fragmentation
  * Linux就是分开存储
* Store in `Block` (1 Block = `1024B` = 1KB)

### One Large File in One Machine: 10GB
* Store in `Chunk` (1 Chunk = `64M` = 64*1024K)
  * Advantage
    * Reduce Metadata Size
  * Disadvantage
    * Waste space for small files
  
### Extra Large File in Several Machine: 10PB
* Key point
  * One Master + Many ChunkServers
    * Chunk Servers = Slave Servers
    * The master don’t record the diskOffset of a chunk
  * Advantage
    * Reduce the size of metadata in master
    * Reduce the traffic between master and ChunkServer(chunk offset改变不需要通知master)
* Master存储10P文件的metadata需要多少容量?
  * 1 chunk = 64MB needs 64B. (经验值) 
  * 10P=16*10^6 chunk needs 10G => 一台机子就可以解决

## One Working Solution for Read/Write
### Write File - 拆分写入
* 一次写入 vs 拆分为多次写入
  * 多次传输: better error tolerance
  * Client自己按照文件大小切分
  * Master分配chunkserver给Client的每个chunk
* 如何写入
  * Client -> Master:  write File_name=/gfs/home/dengchao.mp4, Chunk index=1
  * Master -> Client: Assign Chunkserver_locations=US, CS1
  * Client -> ChunkServer: Transfer Data= /gfs/home/dengchao.mp4-01-of-09
  * ChunkServer -> Master: Write Finish
* Server and Client
Client | Server
--|--
User | Browser
Broswer | Webserver
Webserver | Database
Database | GFS
Webserver | GFS(Google File System)

### Modify File - 重新写入
* One time to write, Many time to read.
  * 先删掉/gfs/home/dengchao.mp4 
  * 重新把整个文件重写一份

### Read File
* 拆分成多份多次读入
* 如何读入
  * Client -> Master: Read File_name=/gfs/home/dengchao.mp4
  * Master -> Client: Return a chunk list.
  * Client -> ChunkServer: Read /gfs/home/dengchao.mp4-00-of-09 in Chunk server 
  * ChunkServer -> Master: Return data /gfs/home/dengchao.mp4-00-of-09
* Master Task
  * 存储各个文件数据的metadata
  * 存储Map(file name + chunk index -> chunk server)
    * 读取时找到对应的chunkserver
    * 写入时分配空闲的chunkserver Task
  * 为什么不把数据直接给master去写?
    * Master bottleneck

## Scale 升级 - 系统如何优化与维护 - GFS的精髓

* 单Master够不够?
  * 工业界90%的系统都采用单master 
  * Simple is perfect
 * Single Pointer of Failure
   * Double Master
   * Multi Master - Paxos Algorithm

### Failure and Recovery - Chechsum, Replica and Heartbeat
* 体检: How to identify failure
  * Checksum Method: MD5, SHA1, SHA256 and SHA512
  * Checksum for Chunk: 
    * 1 checksum = 4B
    * Each chunk (64MB) has a checksum
    * 1P file has 1P/64M*4B=62.5MB
  * 什么时候写入checksum? 
    * 写入一块chunk的时候顺便写入
  * 什么时候去检查checksum?
    * 读入的时候
* 预防: How to avoid failure? 
  * Use Replica
  * 需要多少个备份? 放在哪里?
    * 选3份
    * 两个备份相对比较近，另一个放在较远的地方(2个加州，1个滨州)
  * 选Chunk Server的策略
    * 最近写入比较少的(LRU)
    * 硬盘存储比较低的
* 治疗1: How to recover when chunk is broken?
  * Ask master for help
* 治疗2: How to find whether a ChunkServer is down?
  * Heartbeat: Slave每五分钟告诉Master我还在

### Scale about write
* Client如何写三份?(避免Client bottleneck)
  * Leader-election 
    * 找距离最近的(快)
    * 找现在不干活的(平衡traffic)
  * How to solve ChunkServer failure
    * Retry

## 小结 - Key Point: Master-Slave
* Storage
  * Save a file in one machine -> a big file in one machine -> a extra big file in multi-machine
  * Multi-machine
* How to use the master?
  * How to traffic and storage of master?
* Read:
  * The process of reading a file
* Write:
  * How to reduce master traffic?
    * Client 和 Chunk Server沟通 
  * How to reduce client traffic?
    * Leader Election
* Failure and Recover (key)
  * Discover the failure a chunk?
    * Check Sum
  * Avoid the failure a chunk? 
    * Replica
  * Recover the failure?
    * Ask master
  * Discover the failure of the chunkserver? 
    * Heart Beat
  * Solve the failure of writing ChunkServer?
    * Retry

# Lecture 5 爬虫系统 - Web Crawler & Google Suggestion - 写多读少
## Problem
* URL Parser
* Implement Trie
* Trie-Serialization
* Typeahead
* Webpage Crawler

## Design Web Crawler
* Web Crawler: for collecting data/information from the web

### Scenario: How many web pages? How long? How large?
* Problem:
  * Given seeds, crawl the web
  * Graph traversal problem - Use BFS
* Crawl 1.6M web pages per second
  * 1T web pages
  * Crawl all of them **every week**
* 10P web page storage
  * Average size of a web page: 10K

### Design a Web Crawler
#### A simplistic news crawler
* Input: Given the URL of news list page
* Output: A list of news titles
* Process
  * Send an HTTP request and grab the content of news list page
  * Extract all the news titles from the news list page
```python
import urlib2

url = 'http://tech.163.com/it'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()
```

#### A simplistic crawler
* Input: URL Seeds
* Output: List of URLs

#### A single-threaded web crawler

```python
thread craler
    function run
        while (url_queue not empty) 
            url = url_queue.dequeue()
            html = web_page_loader.load(url) //Consume
            url_list = url_extractor.extract(html) //Produce
            url_queue.enqueue_all(url_list)
        end
```

* Producer-Consumer Model
  * 读写速度不一样所以才需要produce-consume model

#### A multi-threaded web crawler
* Three approaches to sharing resources
  * sleep
  * condition variable (mutex)
  * semaphore
* More threads doesn't mean more performance
  * Context switch cost (CPU number limit)
  * Thread (port) number limitation
  * Network bottleneck for single machine

### Web Crawler小结
* Scenario: How many web pages? How long? How large?
* Service: Crawler, Task Service, StorageService
* Storage: Use db to store tasks, BigTable to store web page
* Scale
  * How to handle Slow Select:
    * Task Table Sharding
  * How to handle Crawler Failure/Update handle (自动调节crawler频率)
    * Exponential crawler
  * How to handle dead cycle? (保证公平性)
    * Use Quota
  * How to handle performance?
    * Multi-region and colocality

## Design a Typeahead System
### Scenario
* Google Suggestion
  * Prefix -> Top N Search Word
  * DAU (daily active user): 500M
  * Search: 4 * 6 * 500M = 12B (every user searches 6 times, types 4 letters)
  * QPS = 12B/86400 = 138k
  * Peak QPS = QPS * 2 = 276k

### Service & Storage
* Service
  * Query Service
  * Data Collection Service
* Storage
  * QueryService: in-memory trie along with disk serialization
  * DataCollectionService: BigTable
* Quality
  * Key metrics: ressponse time
  * Bottom line: result quality

### Scale
* What if the trie gets too large for one machine?
  * Use **consistent** hashing to decide which machine a particular string belongs to
* How to reduce the size of log file?
  * Why? Too time consuming + Too much storage
  * How? Probablistic, log with 1/1000
* How to reduce response time in **front-end**(browser)?
  * Cache result
  * Pre-fetch

# Lecture 6 分布式计算系统 MapReduce
* MapReduce是一套实现分布式运算的框架 
  * Step 1: Input 
  * Step 2: Split
  * Step 3: Map
  * Step 4: 传输整理
  * Step 5: Reduce
  * Step 6: Outpu
* 我们实现什么 - Map和Reduce
```java
public class WordCount {
    public static class Map {
        public void map(String key, String value, OutputCollector<String, Integer> output) {
            String[] tokens = value.split(" ");
            for (String word: tokens) {
                output.collect(word, 1);
            }
        }
    }

    public static class Reduce {
        public void reduce(String key, Iterator<Integer> values, OutputCollector<String, Integer> output) {
            int sum = 0;
            while (values.hasNext()) {
                sum += values.next();
            }
            output.collect(key, sum);
        }
    }
}
```
* Map Reduce Steps
  *Q1: 10PB Data需要几台机器
    * Map: 1000台机器
    * Reduce: 1000台机器
  * Q2: 机器越多越好么？
    * Advantage: 每台处理数据少, 总处理数据越快
    * Disadvantage: 启动机器的时间也边长
  * Q3: 如果不考虑启动时间, Reduce的机器是越多越快么？
    * Key的数目就是reduce的上限
* Shuffle - 传输整理
  * Map Side - Partition and Sort: 硬盘外排序
  * Reduce Side - Fetch and Mergesort: K路归并
* MapReduce application
  * Build Inverted Index
  * Anagram
* Design a MapReduce system

# Lecture 7 地理信息系统 - Location Based System - Yelp, Uber - 写密集的应用

## Problem
* http://www.lintcode.com/problem/mini-yelp/
* http://www.lintcode.com/problem/geohash/
* http://www.lintcode.com/problem/geohash-ii/
* http://www.lintcode.com/problem/mini-cassandra/

* Important Keywords
  * RigPop
  * TChannel
  * Google S2
  * Riak

## Scanraio
* Stage 1
  * Driver report locations - heartbeat
  * Rider requst Uber, match a driver with rider
* Stage 2
  * Driver deny/accept a request
  * Driver cancel a matched request
  * Rider cancel a request
  * Driver pick up a rider/start a trip
  * Driver drop off a rider/end a trip
* Stage 3
  * Uber pool
  * Uber eat
* QPS
  * Driver QPS = 200K driver/ 4s = 50k WRITE
  * Peak Driver QPS = 50k * 3 = 150k WRITE

## Service & Storage
* Service
  * GeoService: 记录车的位置
    * 读少写多
  * Dispatch Service: 匹配打车请求
    * 读多写少
* Storage
  * Trip Table
  * Location Table
### Google S2/Geohash
* Storage
  * Google S2 - 更精准，库函数API丰富
    * Hilbert Curve
    * 将地址空间映射到2^64的整数
    * 如果空间上比较接近的两个点，对应的整数也比较接近
  * Geohash - 比较简单，准确度差一些
    * Peano Curve
    * Base32:0-9, a-z 去掉 (a,i,l,o) 因为视觉上容易搞错
      * 为什么用 base32? 因为刚好2^5, 可以用5位二进制表示，方便计算
    * 核心思路二分法
    * 特性:公共前缀越长，两个点越接近
* How to dispatch
  * Google HQ: 9q9hvu7wbq2s 
    * 找到位置以9q9hv以开头的所有车辆
  * SQL 数据库
    * 首先需要对 geohash 建索引
      * `CREATE INDEX on geohash;`
    * 使用 Like Query
      * `SELECT * FROM location WHERE geohash LIKE` 9q9hv%`;`
  * NoSQL - Cassandra (Treemap)
    * 将 geohash 设为 column key
    * 使用 range query `(9q9hv0, 9q9hvz)`
  * NoSQL - Redis / Memcached (Hashmap)
    * Driver 的位置分级存储
      * 如Driver的位置如果是9q9hvt，则存储在9q9hvt，9q9hv，9q9h这3个key中 
      * 6位geohash的精度已经在一公里以内，对于Uber这类应用足够了
      * 4位geohash的精度在20公里以上了，再大就没意义了，你不会打20公里以外的车
    * key = 9q9hvt, value = set of drivers in this location
  * 选择: NoSQL - Redis
    * 数据可持久化 
    * 原生支持list，set等结构 
    * 读写速度接近内存访问速度 >100k QPS

### Work Solution
* 乘客发出打车请求，服务器创建一次Trip
  * 将 trip_id 返回给用户
  * 乘客每隔几秒询问一次服务器是否匹配成功
* 服务器找到匹配的司机，写入Trip，状态为等待司机回应
  * 同时修改 Driver Table 中的司机状态为不可用，并存入对应的 trip_id
* 司机汇报自己的位置
  * 顺便在 Driver Table 中发现有分配给自己的 trip_id 
  * 去 Trip Table 查询对应的 Trip，返回给司机
* 司机接受打车请求
  * 修改 Driver Table, Trip 中的状态信息 
  * 乘客发现自己匹配成功，获得司机信息
* 司机拒绝打车请求
  * 修改 Driver Table，Trip 中的状态信息，标记该司机已经拒绝了该trip 
  * 重新匹配一个司机，重复第2步

## Scale
* Q: Redis server is down？ (随便挂一台，分分钟损失几百万）
  * A: DB sharding
    * 分摊流量 & Avoid Single Point Failure
  * Q: 按什么进行Sharding?
    * 城市sharding
* Q: How to define city? Geo Fence
  * 用多边形代表城市的范围
  * 人是否在城市 => 点是否在多边形
  * 乘客在边界怎么办？
    * 找2-3个城市, 汇总多个城市的查询结果
* Q: How to check rider is in Airport?
  * Why? 可以进行相应的优惠, 推广,或者限制
  * 分为两级Fence查询，先找到城市，再在城市中查询Airport Fence
* Q: How to reduce impact on db crash?
  * 方法1:Replica by Redis
    * Master - Slave
 *  方法2:Replica by yourself
    * 底层存储的接口将每份数据写3份
    * sharding key 从 123 (city_id) 扩展为
    * 读取的时候，从任意一份 replica 读取数据 
      * 读不到的时候，就从其他的replica读
    * 三份 replica极有可能存在3个不同的机器上，同时挂掉的概率很小很小
      * 当然也有可能不巧存在一个机器上，这个问题如何解决请参考Dynamo DB的论文
  * 方法3:让更强大的NoSQL数据库帮你处理 —— Riak / Cassandra
    * 既然一定需要用多台机器了，那么每台的流量也就没有150k QPS这么高了
    * 用 Riak / Cassandra 等NoSQL数据库，能够帮助你更好的处理 Replica 以及机器挂掉之后恢复的问题

## 总结
* 分析出 Uber 是一个写密集的应用
  * 与大部分应用都是读密集不一样
    * 必须用写比较快的数据库: 例如Redis
    * 或多台数据库
* 解决 LBS 类应用的核心问题 – Geohash / Google S2 
  * 如何存储司机的地理位置
  * 如何查询乘客周围的车
* 分析出一个 Work Solution，说明整个打车的流程 
  * 分析出按照城市进行 Sharding
  * 知道如何做 Geo Fence 的查询
  * 通过分析选择合适的数据库
* 考虑到单点失效(多机)与数据故障(备份)如何解决

# Lecture 8 分布式数据库 - DynamoDB, Big Table
* Big Table - Distributed Database

NoSQL DataBase | Company
--|--
Bigtable | Google
Hbase | Yahoo(Alitaba)Open Source of Bigtable
Cassandra | Facebook
DynamoDB | Amazon

* 文件系统
  * 输入:/home/jinyong/character_name.txt 
  * 输出 : 文件内容
* 数据库系统 - 进阶的文件系统
  * 1. 建立在文件系统之上 
  * 2. 负责组织把一些数据存到文件系统
  * 3. 对外的接口比较方便操作数据
* Scenario - 需求
  * 查询: key (令狐冲 + 颜值) 
  * 返回: value (5)
* Storage
  * 数据最终都会存到文件里面
  * 从文件系统基础上思考 搭建数据库系统
* 写过程
  * 读的时候二分查询 
  * 写的时候写在最后append操作
  * 实现:分块有序
* 分块有序
  * 每一块都是内部有序
  * 写的时候只有最后一块是无序的
    * 读入到内存快速排序
      * Q:机器挂了，内存没了
      * A: Write Ahead Log（非常方便,不需要整理）
* 读过程
  * 建立Index - 加快查询(B tree)
  * 建立Bloom Filter
* Bloom Filter
  * 检查一个key在不在一个File里面
  * False is always false, true may be true
  * 精确度跟什么有关? 
    * 1. 哈希函数个数
    * 2. 位数组长度
    * 3. 加入的字符串数目
* BigTable
  * Sstable: Sorted String Table
    * String is Store in the File
  * SkipList: 用来实现Sorted List
 
* How to read/write key:value from 1PB file
  * Sharding
* How to scale to multiple machines?
  * Master + Slave
  * Master has HashMap[key, server address]
  * Consistent Hashing to Servers
* 机器数据越写越多存不下怎么办
  * 把所有数据存到GFS里面
* Race Conditio between Read/Write?
  * Need a distributed lock
    * Zookeeper (Hadoop)
    * Chubby (Google)
* Distributed Lock
  * The Metadata is store on the Lock
* Bigtable
  * Design: Client + Master + Tablet Server + Distributed Lock
    * Client: Read + Write
    * Tablet Server: Maintain the Data (Key value pairs)
    * Master
      * Shard the file
      * Manage the servers health
    * Distributed Lock
      * Update MetaData
      * Maintain the MetaData
      * Lock Key
  * Optimizaition
    * Write
      * write append
      * Sstable
    * Read
      * Binary Search on Disk
      * Index
      * Bloom filter

# Lecture 9 聊天&访问限制系统

* Problem
  * http://www.lintcode.com/problem/rate-limiter/
  * http://www.lintcode.com/problem/web-logger/
  

## Scenario
* 基本功能:
  * 用户登录注册
  * * 通讯录
  * 两个用户互相发消息
  * 群聊
  * 用户在线状态
* 其他功能
  * 历史消息
  * 多机登陆 Multi Devices

## Service & Storage
* Service
  * Message Service: 负责信息管理
  * Real-time Service: 负责实时推送信息给接受者
* Storage
  * Messsage Table
  * Thread Table "会话"
    * Message vs Threads
      * Inbox has a list of Threads
      * Threads has a list of Messages
    * Threads Table
      * Primary Key: <owner_id, thead_id>
      * Why: 
        * Lots of private field for each owner, like is_blocked, nickname etc
        * Efficient information loading for each user
  * Message Table (NoSQL)
    * 数据量很大，不需要修改，一条聊天信息就像一条log一样
  * Thread Table (SQL) —— 对话表
    * 需要同时 index by
      * Owner ID + Thread ID (primary key)
      * Owner ID + Updated time (按照更新时间倒叙排列)
    * NoSQL 对 secondary index 的支持并不是很好
* Work Solution —— 可行解
  * 用户如何发送消息?
    * Client 把消息和接受者信息发送给 server
    * Server为每个接受者(包括发送者自己)创建一条 Thread (如果没有的话) 
    * 创建一条message(with thread_id)
  * 用户如何接受消息?
    * 可以每隔10秒钟问服务器要一下最新的inbox
      * 虽然听起来很笨，但是也是我们先得到这样一个可行解再说
    * 如果有新消息就提示用户

## Scale
### 实时聊天: Push Service with Socket
* Socket and Push Service
  * Push Service 提供 Socket 连接服务，可以与Client保持TCP的长连接
  * 当用户打开APP之后，就连接上Push Service 中一个属于自己的socket
  * 有人发消息的时候，Message Service 收到消息，通过Push Service把消息发出去
  * 如果一个 用户长期不活跃(比如10分钟)，可以断开链接，释放掉网络端口
  * 断开连接之后，如何收到新消息?
    * 打开APP时主动Pull + Android GCM / IOS APNS
* Socket 链接 与 HTTP 链接的最主要区别是
  * HTTP链接下，只能客户端问服务器要数据
  * Socket链接下，服务器可以**主动**推送数据给客户端

### 群聊: Channel Service
* Problem:
  * 假如一个群有500人(1m用户也同样道理)
    * 如果不做任何优化，需要给这 500 人一个个发消息
    * 但实际上 500 人里只有很少的一些人在线
    * 消息到了Push Server 才发现490个人根本没连上
* Solution: Use Channel Service(知道谁在线)
  * Message Service only send to Channel Service (like a subscription service to threads)
  * Channel Service send to Push Service
* 引入 Push Service 解决实时性问题
* 引入 Channel service 解决群聊问题

### 在线状态 Online Status Update
* 问题
  * 服务器需要知道谁在线谁不在线(push or pull?) 
  * 用户需要知道我的哪些好友在线(push or pull?)
* 解决
  * 每隔10秒告诉服务器我还在，并要一下自己好友的在线状态 
  * 服务器超过1分钟没有收到信息，就认为已经下线

## Design Rate Limiter
* Scenario 场景
  * 根据网络请求的特征进行限制(feature的选取)
    * IP (未登录时的行为), User(登录后的行为), Email(注册，登录，激活)
  * 系统需要做到怎样的程度
    * 如果在某个时间段内超过了一定数目，就拒绝该请求，返回4xx错误 
    * 2/s, 5/m, 10/h, 100/d
    * 无需做到最近30秒，最近21分钟这样的限制。粒度太细意义不大
* Service服务
  * 本身就是一个最小的 Application 了，无法再细分
* Storage 数据存取
  * 需要记录(log)某个特征(feature)在哪个时刻(time)做了什么事情(event)
  * 该数据信息最多保留一天(对于 rate=5/m 的限制，那么一次log在一分钟以后已经没有存在的意义了)
  * 必须是可以高效存取的结构(本来就是为了限制对数据库的读写太多，所以自己的效率必须高与数据库) 
  * 所以使用 Memcached 作为存储结构(数据无需持久化)
* 算法描述
  * 用 event+feature+timestamp 作为 memcached 的key
  * 记录一次访问:
    * 代码:`memcached.increament(key, ttl=60s)`
    * 解释:将对应bucket的访问次数+1，设置60秒后失效
  * 查询是否超过限制
    * 代码
  ```
  for t in 0~59 do
    key = event+feature+(current_timestamp – t)
    sum+= memcahed.get(key, default=0)
  ```
    * Check sum is in limitation
    * 解释:把最近1分钟的访问记录加和
* Scale
  * 问:对于一天来说，有86400秒，检查一次就要 86k 的 cache 访问，如何优化? 
  * 答:分级存储
    * 之前限制以1分钟为单位的时候，每个bucket的大小是1秒，一次查询最多60次读
    * 现在限制以1天为单位的时候，每个bucket以小时为单位存储，一次查询最多24次读
    * 同理如果以小时为单位，那么每个bucket设置为1分钟，一次查询最多60次读

## Design a Datadog 
* Scenario 设计些啥
  * 对于用户对于某个链接的每次访问，记录为一次访问
  * 可以查询某个链接的被访问次数
  * 知道总共多少次访问
  * 知道最近的x小时/x天/x月/x年的访问曲线图
* Service
  * 自身为一个独立的Application，无法更细分
* Storage
  * 基本全是写操作，读操作很少
  * 需要持久化存储(没memcached什么事儿了) 
  * 用NoSQL的话，key 就是 tiny url 的 short_key，value是这个key的所有访问记录的统计数据
  * 核心点是: 多级Bucket
    * 今天的数据，我们以分钟为单位存储
    * 昨天的数据，可能就以5分钟为单位存储
    * 上个月的数据，可能就以1小时为单位存储
    * 去年的数据，就以周为单位存储
  * 用户的查询操作通常是查询某个时刻到当前时刻的曲线图
    * 也就意味着，对于去年的数据，你没有必要一分钟一分钟的进行保存
  * 多级Bucket的思路, 和Rate Limiter如出一辙!
* Scale
  * 问:2k的QPS这么大，往NoSQL的写入操作也这么多么?
    * 答:可以先将最近15秒钟的访问次数 Aggregate 到一起，写在内存里, 每隔15秒将记录写给NoSQL一次，这样写QPS就降到了100多
  * 问:如何将将昨天的数据按照5分钟的bucket进行整理?
    * 答:对老数据进行Aggregate并记录Retention