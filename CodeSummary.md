
# Code Summary

## Table of Content
- [Code Summary](#code-summary)
  - [Table of Content](#table-of-content)
- [Road Map](#road-map)
- [TODO](#todo)
- [Advanced Data Structure Review](#advanced-data-structure-review)
  - [Union-Find Review](#union-find-review)
      - [Review Resources](#review-resources)
      - [Application: Dynamic Connectivity](#application-dynamic-connectivity)
      - [Common Variants](#common-variants)
    - [Template: Disjoint Set Union using Weighted Quick Union UF With Path Compression](#template-disjoint-set-union-using-weighted-quick-union-uf-with-path-compression)
    - [Practice Problem - Disjoint Set Union](#practice-problem---disjoint-set-union)
  - [Binary Search](#binary-search)
    - [Review Notes](#review-notes)
      - [Detailed Explanation on Implementation](#detailed-explanation-on-implementation)
        - [Variant 1 - Basic Binary Search - Reference Only](#variant-1---basic-binary-search---reference-only)
        - [Variant 2 - Reference only](#variant-2---reference-only)
    - [Template: Binary Search](#template-binary-search)
    - [Practice Problem - Binary Search](#practice-problem---binary-search)
- [Hash Table Review](#hash-table-review)
- [Bit Operation Review](#bit-operation-review)
- [Graph Review](#graph-review)
  - [Graph - Undirected Unweighted](#graph---undirected-unweighted)
    - [Representation](#representation)
    - [DFS](#dfs)
      - [DFS Path](#dfs-path)
      - [Connectd Components](#connectd-components)
      - [Cycle](#cycle)
      - [Two-Colorability](#two-colorability)
    - [BFS](#bfs)
      - [BFS Path - Single Source Shortest Path](#bfs-path---single-source-shortest-path)
    - [SymbolGraph](#symbolgraph)
    - [LeetCode Examples](#leetcode-examples)
      - [DFS](#dfs-1)
        - [200 Number of Islands](#200-number-of-islands)
      - [BFS](#bfs-1)
        - [127 WordLadder](#127-wordladder)
        - [126 Word Ladder II](#126-word-ladder-ii)
- [LeetCode Summary](#leetcode-summary)
  - [Calculator I, II, III](#calculator-i-ii-iii)
  - [Sliding Window](#sliding-window)
    - [Template](#template)
      - [Template: Find max substring](#template-find-max-substring)
      - [Template: Find min substring](#template-find-min-substring)
    - [Practice](#practice)
      - [438. Find All Anagrams in a String](#438-find-all-anagrams-in-a-string)
      - [3. Longest Substring without repeating characters](#3-longest-substring-without-repeating-characters)
      - [159. Longest Substring with At Most Two Distinct Characters](#159-longest-substring-with-at-most-two-distinct-characters)
      - [904. Fruit into Basket [Same as 159]](#904-fruit-into-basket-same-as-159)
      - [76. Minimum Window Substring](#76-minimum-window-substring)
  - [Backtrack](#backtrack)
      - [78 Subset](#78-subset)
      - [90 Subset II](#90-subset-ii)
      - [46 Permutation](#46-permutation)
      - [47 Permutation II](#47-permutation-ii)
      - [51 NQueens](#51-nqueens)
      - [52 NQueens II](#52-nqueens-ii)
      - [39 Combination Sum](#39-combination-sum)
      - [40 Combinaiton Sum II](#40-combinaiton-sum-ii)
      - [216 Combination Sum III](#216-combination-sum-iii)
      - [37 Soduku Solver](#37-soduku-solver)
- [Compiler Template Review](#compiler-template-review)
  - [Calculator I, II, III](#calculator-i-ii-iii-1)
    - [High Level Design](#high-level-design)
    - [Chosen Design](#chosen-design)
- [Tree Review](#tree-review)
  - [Binary Index Tree (Fenwick Tree)](#binary-index-tree-fenwick-tree)
      - [BIT Template](#bit-template)
  - [Trie](#trie)
  - [Dynamic Programming Review](#dynamic-programming-review)
    - [Overview](#overview)
    - [Pattern 1: Minimum Path to Reach a Target](#pattern-1-minimum-path-to-reach-a-target)
      - [**Template**](#template-1)
      - [Practice Questions](#practice-questions)
    - [Pattern 2: Distinct Ways](#pattern-2-distinct-ways)
      - [**Template**](#template-2)
      - [Practice Questions](#practice-questions-1)
    - [Pattern 3: Merging Intervals](#pattern-3-merging-intervals)
      - [**Template**](#template-3)
      - [Practice Questions](#practice-questions-2)
    - [Pattern 4: DP on Strings](#pattern-4-dp-on-strings)
      - [**Template**](#template-4)
      - [Practice Questions](#practice-questions-3)
    - [Pattern 5: Making Decisions](#pattern-5-making-decisions)
      - [**Template**](#template-5)
      - [Practice Questions](#practice-questions-4)

# Road Map

Topics |Data Structure and Algorithm
--|--
Data Types | stack, queue, bag, **union-find**, priority queue
Sorting | quicksort, mergesort, heapsort, radix sorts
Searching | BST, red-black BST, hash table
Graphs | BFS, DFS, Prim, Kruskal, Dijkstra
Strings | KMP, regular expressions, tries, data compression
Advanced | B-tree, k-d tree, suffix array, maxflow

# TODO

TODO 1: Add review for trees

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

Read HashSet Implementation https://leetcode.com/problems/design-hashset/solution/

TODO 7:
Understand Parser/Lexer etc (LeetCode 640, 536, PythonInterpreter, LeetCode Brace Expansion 1&2)

TODO 8:
Read Philosophy here: https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp 
Summarize Dynamic Programming Patterns: https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns


# Advanced Data Structure Review

## Union-Find Review

#### Review Resources
* Read Princeton's [union-find review notes](https://algs4.cs.princeton.edu/15uf/) with [code implementation](https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionPathCompressionUF.java.html)
* Read Princeton's [union-find slides](https://algs4.cs.princeton.edu/lectures/15UnionFind-2x2.pdf) and optionally [watch video](https://www.bilibili.com/video/av55943680?p=3)


#### Application: Dynamic Connectivity

Given a set of N objects, support two operation:
* Connect two objects
* Is there a path connecting the two objects?

#### Common Variants

 Variant | initialize | union | find | Worst case for M ops | Note
--|--|--|--|--|--|--
quick-find(eager approach) | $O(N)$ | $O(N)$ | 1 | $MN$ | **Union**: To merge components containing p and q, change all entries whose id equals id[p] to id[q].
quick-union(lazy approach) | $O(N)$ | $O(N)$ | $O(N)$ | $MN$ | **Union**: To merge components containing p and q, change root of p to root of q.  ***Tree might be too tall*** 
weighted quick-union | $O(N)$ | $O(lg N)$ | $O(lg N)$  | $N + M log N$ | **Key Idea**: Mantain a size array. Smaller tree is merged to larger tree to maintain balance
quick-union with path compression | $O(N)$ | $O(lg N)$  | $O(lg N)$  | $N + M log N$| **Key Idea**: Flat out the children to parent
weighted quick-union with path compression | $O(N)$ | $O(\alpha(N))$  | $O(\alpha(N))$  | $N + M \alpha(N) \approx N + M$  | $\alpha$ is the Inverse-Ackermann function, and $O( \alpha(N)) \approx O(1)$

### Template: Disjoint Set Union using Weighted Quick Union UF With Path Compression

```java
    //Weighted Quick-Union UF With Path Compression
    //O(alpha N) - Inverse-Ackermann of N, approximately O(1)
    public class DSU {
        private int[] parent; // parent[i] = parent of i
        private int[] size; // IMPROVEMENT: use weight, size[i] = number of sites in tree rooted at i
        private int count; //number of components

        public DSU(int N) { 
            count = N;
            parent = new int[N];
            size = new int[N];
            for (int i = 0; i < N; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        //Original: return the root
        //Improvemnt: Find root first, then point all nodes along the path to root.
        public int find(int i) {
            //Find root
            int root = i;
            while (root != parent[root]) {
                root = parent[root];
            }      
            //IMPROVE: point all nodes along the path to root
            while (i != root) {
                int nextI = parent[i];
                parent[i] = root;
                i = nextI;
            }
            return root;
        }

        //Original: change root of p to point to root of q
        //Improvement: point root of smaller tree to larger tree
        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) {
                return;
            }
            // IMPROVE: make smaller **root** point to larger **root**
            if (size[rootP] < size[rootQ]) {
                parent[rootP] = rootQ;
                size[rootQ] += size[rootP];
            }
            else {
                parent[rootQ] = rootP;
                size[rootP] += size[rootQ];
            }
            count--;
        }

        //Get number of connected components
        public int count() {
            return count;
        }
    }
```

### Practice Problem - Disjoint Set Union
* [LeetCode Union-Find Tag](https://leetcode.com/tag/union-find/)
* [LC323 Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
* [LC684 Redundant Connection](https://leetcode.com/problems/redundant-connection/solution/)
* [LC1101 The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/)
* [LC947 Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/)
* [LC721 Accounts Merge](https://leetcode.com/problems/accounts-merge/solution/)
* [LC737 Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/solution/)

## Binary Search

### Review Notes
* For out-of-box binary search, use Java's `Arrays.binarySearch()`
  * It returns index of the search key, if it is contained in the array; otherwise, (-(insertion point) – 1). This gurantees that the return value will be >= 0 if and only if the key is found.
  * If the array is not sorted, the results are undefined. 
  * If the array contains multiple elements with the specified value, there is no guarantee which one will be found.

* For my binary search implementation below
  * It returns the *first* occurence of target in the array, or position to be inserted
  * Keypoint: Maintain `A[low] <= key < A[high]`, check to move `low` and return `low`.


#### Detailed Explanation on Implementation

This section is for reference only. It helps me to memorize all the different boundary condition. 

* Assumption: Array sorted, **might contain duplicate**
* Invariant: `A[low] <= target < A[high]`
* Returns: The *first* occurence of target in the array, or position to be inserted
* This is based on variant 1

```java
    //Invariant: A[low] <= target < A[high]
    public static int binarySearch(int[] A, int target) {
        int low = 0, high = A.length; //NOTE: A.length since invariant is key < A[high]
        while (low < high) { //NOTE: Not '<=' since the invariant A[low] < A[high]
            int mid = low + (high - low)/2;
            if (target > A[mid]) { //NOTE: Check to move low pointer
                low = mid + 1; //NOTE: must increase mid by 1, compare to Variant 2 
            } else { //NOTE: merge the equal case and move high pointer case to get first occurence. Can split out the equal case and return early if no duplicate. See variant 1
                high = mid; //NOTE: do not decrease mid by 1, since the invariant is target < A[high]. 
                //NOTE: High always decreases, even when high-low==1, in this case, mid = low, so high == low, therefore exit the circle
            }
        }
        return low; // low is position where target would be inserted, or -1 for not found
    }
```

##### Variant 1 - Basic Binary Search - Reference Only

* Assumption: Array sorted, **no duplicate**
* Invariant: `A[low] <= target < A[high]`

```java
    //Invariant: A[low] <= target < A[high]
    //Return the index of target, or the position it would be inserted
    public static int binarySearch(int[] A, int target) {
        int low = 0, high = A.length; //DIFF1: mid != high, so it must be outside
        while (low < high) { //DIFF: Not the invariant is different now
            int mid = low + (high - low)/2;
            //3-way comparison
            if (target < A[mid]) {
                high = mid; //DIFF: don't decrease by 1, since mid != high
            } else if (target > A[mid]) {
                low = mid + 1;
            } else {
                return mid; //NOTE: Change to high = mid to get the first occurence
            }
        }
        return low;
    }
```

* NOTE: to get the first occurence of target for arrays containing duplicates, simply merge the 

##### Variant 2 - Reference only

* Assumption: Array sorted, and **no duplication**
* Invariant: `A[low] <= target <= A[high]`
* This is the version in Princeton's algorithm course. Note the invariant is different

 ```java
    //Invariant: A[low] <= key <= A[high]
    //Return the index of target, or the position it would be inserted
    //Assumption
    public static int binarySearch(int[] A, int target) {
        int low = 0, high = A.length - 1; //NOTE: high = A.length - 1 to make sure A[high] is valid
        while (low <= high) { //NOTE: maintain invariant, so it's '<=', not '<'
            int mid = low + (high - low)/2; //NOTE: avoid overflow, don't do (low+high)/2
            if (target < A[mid]) {
                high = mid - 1; //NOTE: must decrease by 1, otherwise will deadloop when high == mid
            } else if (target > A[mid]) {
                low = mid + 1; //NOTE:increase by 1
            } else {
                return mid; //Set high = mid here instead of returning if A contains duplicate
            }
        }
        return low; //NOTE: return low (insertion pos) or -1 (doesn't exist)
    }
```

### Template: Binary Search

```java
    //Invariant: A[low] <= target < A[high]
    //Return first occurence of target, or position it should be inserted
    public static int binarySearch(int[] A, int target) {
        int low = 0, high = A.length;
        while (low < high) { //Invariant hold
            int mid = low + (high - low) / 2;
            if (target > A[mid]) { //Check to move low
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
```

### Practice Problem - Binary Search
* [EASY] [LC704 Binary Search](https://leetcode.com/problems/binary-search/)
* [EASY] [LC35 Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [EASY] [LC1150 Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/submissions/)


# Hash Table Review

Read Wikipedia [Hash Table](https://en.wikipedia.org/wiki/Hash_table) for details and implement [LC705 HashSet ](https://leetcode.com/problems/design-hashset/solution/) as coding practicse. 

There are two key questions that one should address, in order to implement the HashSet data structure, namely **hash function** and **collision handling**. Additionally we can also discuss **dynamic resizing**

* **Hash Function**: the goal of the hash function is to assign an address to store a given value. Ideally, each unique value should have an unique hash value.
  * **Load factor**: A critical statistic for a hash table is the load factor, 
    $$\text{load factor} = \frac {n} {k}$$ 

    * n is the number of entries occupied in the hash table.
    * k is the number of buckets.
    *  As a real-world example, the default load factor for a HashMap in Java 10 is 0.75, which "offers a good trade-off between time and space costs."
 
* **Collision Resolution**: since the nature of a hash function is to map a value from a space A into a corresponding value in a smaller space B, it could happen that multiple values from space A might be mapped to the same value in space B. This is what we call collision. Therefore, it is indispensible for us to have a strategy to handle the collision.
  * **Separate Chaining**: for values with the same hash key, we keep them in a bucket, and each bucket is independent from each other
  * **Open Addressing**: whenever there is a collision, we keep on probing on the main space with certain strategy until a free slot is found. Well-known probing strategies
    * **Linear probing**, in which the interval between probes is fixed (usually 1)
    * **Quadratic probing**, in which the interval between probes is increased by adding the successive outputs of a quadratic polynomial to the starting value given by the original hash computation
    * **Double hashing**, in which the interval between probes is computed by a second hash function
  * **2-Choice Hashing**: we use two hash functions rather than one, and we pick the generated address with fewer collision.
* **Dynamic Resizing**: When an insert is made such that the number of entries in a hash table exceeds the product of the load factor and the current capacity then the hash table will need to be rehashed.
  * **All-At-Once Rehashing**: Automatically trigger a complete resizing when the load factor exceeds some threshold


# Bit Operation Review

Bitwise note

* `num | (1<<k)`: set num's k-th bit as 1
* `num & (1<<k)`: get num's k-th bit
* `num ^ (1<<k)`: flip num's k-th bit
  * See Leetcode 1066 Campus Bike II
* `index & (-index)`: get lowest set bit (useful for Fenwick Tree)

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

## Calculator I, II, III

Here's a generic calculator using context free grammar

```java
/*
https://ruslanspivak.com/lsbasi-part8/

New Case:
"7 + 3 * (10 / (12 / (3 + 1) - 1))" ==> 22

Parser / Interpreter

expr -> term ((PLUS|MINUS) term)*
term -> factor ((MUL|DIV) factor)*
factor -> （PLUS|MINUS）FACTOR | INTEGER | LPAREN expr RPAREN

*/
class Solution {
    public enum Type {
            PLUS, MINUS,
            MUL, DIV,
            LPAREN, RPAREN,
            INTEGER,
            EOF //End of file  
    }
    
    class Token {
        private Type type;
        private int value;
        
        Token(Type type, int value) {
            this.type = type;
            this.value = value;
        }
        
        public String toString() { 
            return "("+type+","+value+")"; 
        }
    }
    
    class Lexer {
        private String text;
        private int pos;
        private char currentChar;
        private static final char NONE = '$';
        
        Lexer(String text) {
            this.text = text;
            this.pos = 0; //Current position to be consumed
            this.currentChar = text.charAt(pos);
        }
        
        private void advance() {
            pos++;
            if (pos == text.length()) {
                currentChar = NONE;
            } else {
                currentChar = text.charAt(pos);
            }
        }
        
                
        private void skipWhitespace() {
            while (currentChar != NONE && Character.isSpace(currentChar)) {
                advance();
            }
        }
        
        private int integer() {
            int result = 0;
            while (currentChar != NONE && Character.isDigit(currentChar)) {
                result = result * 10 + (currentChar - '0');
                advance();
            }
            return result;
        }
        
        public Token getNextToken() {
            while (currentChar != NONE) {
                if (Character.isSpace(currentChar)) {
                    skipWhitespace();
                    continue;
                } else if (Character.isDigit(currentChar)) {
                    return new Token(Type.INTEGER, integer());
                } else if (currentChar == '+') {
                    advance();
                    return new Token(Type.PLUS, 0);
                } else if (currentChar == '-') {
                    advance();
                    return new Token(Type.MINUS, 0);
                } else if (currentChar == '*') {
                    advance();
                    return new Token(Type.MUL, 0);
                } else if (currentChar == '/') {
                    advance();
                    return new Token(Type.DIV, 0);
                } else if (currentChar == '(') {
                    advance();
                    return new Token(Type.LPAREN, 0);
                } else if (currentChar == ')') {
                    advance();
                    return new Token(Type.RPAREN, 0);
                } else {
                    System.out.println("LEXER: Invalid Character: " + currentChar);
                }
                
            }
            return new Token(Type.EOF, 0);
        }
    }
    
    class Interpreter {
        private Lexer lexer;
        private Token currentToken;
        
        Interpreter(Lexer lexer) {
            this.lexer = lexer;
            this.currentToken = lexer.getNextToken();
        }
        
        private void eat(Type tokenType) {
            //System.out.println(currentToken);
            if (currentToken.type != tokenType) {
               System.out.println("Invalid Syntax: Expected token: " + tokenType + ", actual token " + currentToken.type);
            }
            currentToken = lexer.getNextToken();
        }
        
        private int expr() {
            //set current token to the first token taken from the input
            int result = term();

            while (currentToken.type == Type.PLUS || currentToken.type == Type.MINUS) {
                Token token = currentToken;
                if (token.type == Type.PLUS) {
                    eat(Type.PLUS);
                    result =  result + term();
                } else if (token.type == Type.MINUS) {
                    eat(Type.MINUS);
                    result =  result - term();
                }
            }
            return result;
        }

        private int term() {
            int result = factor();
            while (currentToken.type == Type.MUL || currentToken.type == Type.DIV) {
                Token token = currentToken;
                if (token.type == Type.MUL) {
                    eat(Type.MUL);
                    result = result * factor();
                } else if (token.type == Type.DIV) {
                    eat(Type.DIV);
                    result = result / factor();
                } 
            }
            return result;
        }

        private int factor() {
            Token token = currentToken;
            if (token.type == Type.PLUS) {
                eat(Type.PLUS);
                return factor();
            } else if (token.type == Type.MINUS) {
                eat(Type.MINUS);
                return -1 * factor();
            } else if (token.type == Type.INTEGER) {
                eat(Type.INTEGER);
                return token.value;
            } else if (token.type == Type.LPAREN) {
                eat(Type.LPAREN);
                int result = expr();
                eat(Type.RPAREN);
                return result;
            }
            System.out.println("Invalid Syntax in factor()");
            return -1; //Should never reach here
        }
    }
    
    public int calculate(String text) {
        Lexer lexer = new Lexer(text);
        Interpreter interpreter = new Interpreter(lexer);
        int result = interpreter.expr();
        return result;
    }
}
```


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

```java
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

#### 37 Soduku Solver
```java
class Solution {
    public void solveSudoku(char[][] board) {
        if (board ==  null || board.length == 0) {
            return;
        }
        backtrack(board, 0, 0);
    }
    
    private boolean backtrack(char[][] board, int row, int col) {
        for (int i = row; i < 9; i++, col = 0) { //Must reset col here, so in next row, it starts from first col again
            for (int j = col; j < 9; j++) {
                if (board[i][j] != '.') {
                    continue;
                }
                for (char c = '1'; c <= '9'; c++) {
                    if (isValid(board, i, j, c)) {
                        board[i][j] = c;
                        if (backtrack(board, i, j+1)) {
                            return true;
                        } 
                        board[i][j] = '.';
                        
                    }
                }
                return false;
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, int row, int col, char c) {
        int blockRow = (row/3) * 3, blockCol = (col/3)*3;
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c  //Check row
                || board[row][i] == c  //Check col
                || board[blockRow+i/3][blockCol+i%3] == c //Check 3*3 block
               ) {
                return false;
            }
        }
        return true;
    }
}
```

# Compiler Template Review

## Calculator I, II, III

Here's my template for solving compiler type of quesitons. Here's how to do Calculator III

### High Level Design

`<Text> -> Lexer -> <Token> -> Parser -> <AST> -> Interpreter -> <Result>`

A working full version to implement calculator is here: https://github.com/cookieisaac/interpreter/blob/master/calc8.java

Note how the Parser generates AST Node, an Intermediate Representation, instead of result. Also note how the interpreter is using visitor pattern to access the Node to evaluate

### Chosen Design

And we don't need to care about semantics, so I skipped AST in implementation, and we only do  

`<Text> -> Lexer -> <Token> -> Parser/Interpreter -> <Result>`

* Key API for Lexer is `advance()` and `getNextToken()`: generate all the terminal symbols

* Key API for Parser is `eat()` and each `Context-Free Grammar` rule

Our calculator is essentially a `recursive descent` parser, a kind of top-down parser built from a set of mutually recursive procedures (or a non-recursive equivalent) where each such procedure implements one of the *nonterminals* of the grammar. 

For calculator, the extended Backus–Naur form (EBNF) for calculator are as follow
```
expr -> term ((PLUS|MINUS) term)*
term -> factor ((MUL|DIV) factor)*
factor -> （PLUS|MINUS）FACTOR | INTEGER | LPAREN expr RPAREN
```

A working version is implemented here:  https://github.com/cookieisaac/interpreter/blob/master/LC772_BasicCalculatorIII.java

Here is the template for [Basic Calculator I](https://leetcode.com/problems/basic-calculator/), memorize this, and see how easy it is to extend to calculator II and calculator III.

```java
/*
expr: term ((PLUS | MINUS) term) *
term: LPAREN expr RPAREN | INTEGER
*/
class Solution {
    public enum Type {
        PLUS, MINUS,
        LPAREN, RPAREN,
        INTEGER,
        ERROR, EOF
    }
    
    public class Token {
        private static final int NAN = -1;
        
        Type type;
        int value;
        
        Token(Type type) {
            this.type = type;
            this.value = NAN;
        }
        
        Token(Type type, int value) {
            this.type = type;
            this.value = value;
        }
    }
    
    public class Lexer {
        private int pos;
        private char currentChar;
        private String text;
        private char NONE = '$';
        
        Lexer(String s) {
            this.text = s;
            this.pos = 0;
            this.currentChar = text.charAt(pos);
        }
        
        private void advance() {
            pos++;
            currentChar = pos < text.length() ? text.charAt(pos) : NONE;
        }
        
        private void skipWhitespace() {
            while (currentChar != NONE && Character.isSpace(currentChar)) {
                advance();
            }
        }
        
        private int integer() {
            int result = 0;
            while (currentChar != NONE && Character.isDigit(currentChar)) {
                result = result*10 + (currentChar - '0');
                advance();
            } 
            return result;
        }
        
        public Token getNextToken() {
            while (currentChar != NONE) {
                if (Character.isSpace(currentChar)) {
                    skipWhitespace();
                    continue;
                } else if (Character.isDigit(currentChar)) {
                    return new Token(Type.INTEGER, integer());
                } else if (currentChar == '+') {
                    advance();
                    return new Token(Type.PLUS);
                } else if (currentChar == '-') {
                    advance();
                    return new Token(Type.MINUS);
                } else if (currentChar == '(') {
                    advance();
                    return new Token(Type.LPAREN);
                } else if (currentChar == ')') {
                    advance();
                    return new Token(Type.RPAREN);
                } else {
                    System.out.println("LEX ERROR: invalid character " + currentChar);
                    currentChar = NONE;
                }
            }
            return new Token(Type.EOF);
        }
    }
    
    //Parser/Interpreter
    class Parser {
        Lexer lexer;
        Token currentToken;
        
        Parser(Lexer lexer) {
            this.lexer = lexer;
            this.currentToken = lexer.getNextToken();
        }
        
        private void eat(Type type) {
            if (currentToken.type != type) {
                System.out.println("SYNTAX ERROR: expecting " + type + ", acutal " + currentToken.type);
            }
            //System.out.println("Consuming " + type);
            currentToken = lexer.getNextToken();
        }
        
        private int term() {
            Token token = currentToken;
            if (token.type == Type.INTEGER) {
                int result = token.value;
                eat(Type.INTEGER);
                return result;
            } else if (token.type == Type.LPAREN) {
                eat(Type.LPAREN);
                int result = expr();
                eat(Type.RPAREN);
                return result;
            }
            System.out.println("SYNTAX ERROR: term() should never reach here " + token.type);
            return -1;
        }
        
        private int expr() {
            int result = term();
            while (currentToken.type == Type.PLUS || currentToken.type == Type.MINUS) {
                Token token = currentToken;
                if (token.type == Type.PLUS) {
                    eat(Type.PLUS);
                    result += term();
                } else if (token.type == Type.MINUS) {
                    eat(Type.MINUS);
                    result -= term();
                } else {
                    System.out.println("SYNTAX ERROR: expr() should never reach here");
                }
            }
            return result;
        }
        
        public int parse() {
            return expr();
        }
    }
    
    public int calculate(String s) {
        Lexer lexer = new Lexer(s);
        Parser parser = new Parser(lexer);
        return parser.parse();
    }
}
```


# Tree Review

## Binary Index Tree (Fenwick Tree)

Introduction to Binary Index Tree: 
* [Tushar's Video Tutorial](https://www.youtube.com/watch?v=CWDQJGaN1gY): Good mechanical. The tree Tushar draw is the query tree. See Huahua's video for both query tree and update tree
* [Huahua's Video Tutorial](https://www.youtube.com/watch?v=WbafSgetDDk): Good visualization of update tree and query tree
* [Geek for geek: Blogpost on detailed explanation](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/): why `i&(-i)` is for lowest set bit


![alt text](https://zxi.mytechroad.com/blog/wp-content/uploads/2018/01/sp3-2.png)

Binary Index Tree is designed specifically for [LC 307 Range Sum Query - mutable](https://leetcode.com/problems/range-sum-query-mutable/)

* Query: `O(log N)`
* Update: `O(log N)`
* First time construction: `O(N log N)`
* Space: `O(N)`

Compared to *Binary Search Tree*, it is guranteed to be balanced. Compared to *Segment Tree*, it is easy to implement and more performant.



#### BIT Template
```java
    class FenwickTree {
        private int[] tree;

        FenwickTree(int[] nums) {
            this.tree = new int[nums.length + 1];
            for (int index = 0; index < nums.length; index++) {
                update(index, nums[index]);
            }
        }

        // the index is the index of original array
        public void update(int index, int delta) {
            // the index of fenwick tree is one larger than the index of original array
            for (int i = index + 1; i < tree.length; i += i & (-i)) {
                tree[i] += delta;
            }
        }

        // Input: the index is the index of original array.
        // Returns: sum from 0 to index (inclusive)
        public int querySum(int index) {
            int sum = 0;
            // the index of fenwick tree is one larger than the index of original array
            for (int i = index + 1; i > 0; i -= i & (-i)) {
                sum += tree[i];
            }
            return sum;
        }
    }
```

Good Read for Recursion: https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22

Similar Problem: 
* Range Sum Query
```java
class NumArray {
    int[] nums;
    int N;
    FenwickTree tree;
    
    class FenwickTree {
        private int[] tree;

        FenwickTree(int[] nums) {
            this.tree = new int[nums.length + 1];
            for (int index = 0; index < nums.length; index++) {
                update(index, nums[index]);
            }
        }

        // the index is the index of original array
        public void update(int index, int delta) {
            // the index of fenwick tree is one larger than the index of original array
            for (int i = index + 1; i < tree.length; i += i & (-i)) {
                tree[i] += delta;
            }
        }

        // Input: the index is the index of original array.
        // Returns: sum from 0 to index (inclusive)
        public int querySum(int index) {
            int sum = 0;
            // the index of fenwick tree is one larger than the index of original array
            for (int i = index + 1; i > 0; i -= i & (-i)) {
                sum += tree[i];
            }
            return sum;
        }
    }
    
    public NumArray(int[] nums) {
        this.nums = nums;
        this.N = nums.length;
        this.tree = new FenwickTree(nums);
    }
    
    public void update(int i, int val) {
        int delta = val - nums[i];
        nums[i] = val; //Do forget update nums, otherwise future delta will be wrong
        tree.update(i, delta);   
    }
    
    public int sumRange(int i, int j) {
        return tree.querySum(j) - tree.querySum(i-1);
    }
}
```

* 493. Reverse Pairs
* [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76611/Short-Java-Binary-Index-Tree-BEAT-97.33-With-Detailed-Explanation/80347)
```java
public class Solution {
    public List<Integer> countSmaller(int[] nums) {
        if(nums == null || nums.length == 0) return new ArrayList<>();
        
        // clone the original array and sort it, store <value, position> into hash map
        Map<Integer, Integer> map = new HashMap<>();
        int[] sortedNum = nums.clone();
        Arrays.sort(sortedNum);
        for(int i = 0; i < nums.length; i++) map.put(sortedNum[i], i);
        
        // create fenwick tree whose length is one larger than the original array
        int[] fenwickTree = new int[nums.length + 1];
        List<Integer> res = new ArrayList<>();
        for(int i = nums.length - 1; i >= 0; i--) {
            res.add(0, getSum(fenwickTree, map.get(nums[i]) - 1));
            updateFenwickTree(fenwickTree, map.get(nums[i]), 1);
        }
        return res;
    }

    // the index is the index of original array
    private void updateFenwickTree(int[] fenwickTree, int index, int delta) {
        // the index of fenwick tree is one larger than the index of original array
        for(int i = index + 1; i < fenwickTree.length; i += i & (-i)) {
            fenwickTree[i] += delta;
        }
    }

    // the index is the index of original array
    private int getSum(int[] fenwickTree, int index) {
        int sum = 0;
        // the index of fenwick tree is one larger than the index of original array
        for(int i = index + 1; i > 0; i -= i & (-i)) {
            sum += fenwickTree[i];
        }
        return sum;
    }
}
```
* 

## Trie


## Dynamic Programming Review


### Overview

**Resources**
* [Leetcode Post: My experience and notes for learning dp](https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp)

**Summary**

Based on [the great summary here](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns#distinct-ways), there are five patterns in dynamic programming so far.

* 1. Minimum (Maximum) Path to Reach a Target
* 2. Distinct Ways
* 3. Merging Intervals
* 4. DP on Strings
* 5. Decision Making

**Note** 
- Pattern 1 and Pattern 2 are very similar
- Pattern 3 problems is that they usually involve a list/array of numbers, either explicitly or implicity, like in LC1130, LC96 and LC1039.

### Pattern 1: Minimum Path to Reach a Target

* **Problems**: Given a target, find minimum (maximum) cost / path / sum to reach the target. 
* **Examples**: Coin Change, Min Path Sum and Min Cost Climbing Stairs
* **Approach**:
Choose minimum (maximum) path among all possible paths before the current state, then add value for the current state.
```
routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]
```
#### **Template**
Generate optimal solutions for all values in the target and return the value for the target.
```java
//Build from smaller target
for (int i = 1; i <= target; ++i) {
    //Try all different ways
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] = min(dp[i], dp[i - ways[j]]) + cost / path / sum;
       }
   }
}
 
return dp[target];
```

#### Practice Questions
* [`MEDIUM`][LC322 Coin Change](https://leetcode.com/problems/coin-change/)
```java
        int[] dp = new int[amount + 1];
        int MAX_VALUE = amount+1; //Don't use Integer.MAX_VALUE, otherwise will overflow to negative number when add by 1
        
        Arrays.fill(dp, MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] == MAX_VALUE ? -1: dp[amount];
    }
```

* [`EASY`] [LC746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/submissions/) 
```java
        //Init base case
        dp[0] = cost[0]; dp[1] = cost[1];
        //Fill DP
        for (int i = 2; i <= N; i++) {
            dp[i] = Math.min(dp[i-1], dp[i-2]) + (i == N ? 0 : cost[i]);
        }
```
* [`MEDIUM`] [LC64 Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
```java
        //Init base case
        for(int i = 1; i < M; i++) {
            grid[i][0] += grid[i-1][0];
        }
        for (int j = 1; j < N; j++) {
            grid[0][j] += grid[0][j-1];
        }
        
        //Fill in DP
        for (int i = 1; i < M; i++) {
            for (int j = 1; j < N; j++) {
                grid[i][j] = Math.min(grid[i-1][j], grid[i][j-1]) + grid[i][j];
            }
        }
        return grid[M-1][N-1];
```

* TODO: Summarize
```
931. Minimum Falling Path Sum Medium

983. Minimum Cost For Tickets Medium

650. 2 Keys Keyboard Medium

279. Perfect Squares Medium

1049. Last Stone Weight II Medium

120. Triangle Medium

474. Ones and Zeroes Medium

221. Maximal Square Medium

322. Coin Change Medium

1240. Tiling a Rectangle with the Fewest Squares Hard

174. Dungeon Game Hard

871. Minimum Number of Refueling Stops Hard
```

### Pattern 2: Distinct Ways

* **Problems**: Given a target, find the number of distinct ways to reach the target.
* **Examples**: Climbing Stairs, Unique Paths
* **Approach**:
Sum all possible ways to reach the current state.
```
routes[i] = routes[i-1] + routes[i-2], ... , + routes[i-k]
```

#### **Template**

* Note: Just change the `min` operation from previous template to `+` here

Generate sum for all values in the target and return the value for the target.
```java
//Build from smaller target
for (int i = 1; i <= target; ++i) {
    //Try all different ways
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] += dp[i - ways[j]];
       }
   }
}
 
return dp[target];
```

#### Practice Questions

* [`EASY`] [LC70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
  * Note: Compare to [LC746 Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/), just change min to plus.
```java
    //Init base
    dp[0] = 1;dp[1] = 1;
    //Fill DP
    for (int stair = 2; stair <= n; stair++) {
        for (int step = 1; step <= 2; step++) {
            dp[stair] += dp[stair-step];
        }
    }
```

* [`MEDIUM`] [LC62 Unique Paths](https://leetcode.com/problems/unique-paths/)
  * Note: Compare to [LC64 Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/), just change min to plus.
```java
        //Init base - first row and first col
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        //Fill DP
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
```

* [`MEDIUM`] [LC1155 Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
  * Note: Add one for loop for repetition of rolling dices. Assuming d is constant, then the problem is reduced to count of distinct ways
  * If we don't consider the dice dimension, then it is just the climbing stairs problem where we can step at most 6 steps.

```java
long[][] dp = new long[dice+1][target + 1]; 
for (int d = 1; d <= dice; d++) {
    //--Template start from here
    for (int t = 0; t <= target; t++) {
        for (int f = 1; f <= face; f++) {
            if ( f <= t) {
                dp[d][t] += dp[d-1][t-f];
                dp[d][t] %= MOD;
            } else {
                break;
            }
        }
    }
    //---Template end here---
}
```

* TODO Summarize
```
688. Knight Probability in Chessboard Medium

494. Target Sum Medium

377. Combination Sum IV Medium

935. Knight Dialer Medium

1223. Dice Roll Simulation Medium

416. Partition Equal Subset Sum Medium

808. Soup Servings Medium

790. Domino and Tromino Tiling Medium

801. Minimum Swaps To Make Sequences Increasing

673. Number of Longest Increasing Subsequence Medium

63. Unique Paths II Medium

576. Out of Boundary Paths Medium

1269. Number of Ways to Stay in the Same Place After Some Steps Hard

1220. Count Vowels Permutation Hard
```

### Pattern 3: Merging Intervals

* **Problems**: Given *a set of numbers*, find an optimal solution for a problem considering the current number and the best you can get from the left and right sides.
* **Examples**: Bursting Balloons, Merge Stones
* **Approach**:
Find all optimal solutions for every interval and return the best possible answer.

```
int j = i + len; // Sub-interval [i, j) is of size len
dp[i][j] = dp[i][k] + result[k] + dp[k+1][j]
```

#### **Template**

Get the best from the left and right sides and add a solution for the current position.

```java
for (int len = 1; len < N; len++) { //Length of interval
    for (int i = 0; i < N - len; i++) { //Solve for all intervals [i, j) of length len
        int j = i + len;
        dp[i][j] = Integer.MAX_VALUE;
        for (int k = i; k < j; k++) { //Divide to [i, k), [k], [k+1, j)
            dp[i][j] = min(dp[i][j], dp[i][k] + result[k] + dp[k+1][j]);
        }
    }
}
return dp[0][N-1];
```

NOTE: Clearly define whether `dp[i][j] `stores `[i, j]` or `[i, j)`. This has significant impact on the boundary condition.

#### Practice Questions

* [`MEDIUM`] [LC1130 Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)

```java
        //DP: merging intervals
        for (int len = 1; len < N; len++) { //len of interval [i, j), stores in dp[i][j]
            for (int i = 0; i < N - len; i++) {
                int j = i + len;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], 
                       dp[i][k] + dp[k+1][j] + max[i][k] * max[k+1][j]);
                }
            }
        }
```

This problem is only a practise for DP. A better solution is O(N) based on stack as explained here.

  * TODO Summarize Stacks
```java
More Good Stack Problems
Here are some problems that impressed me.
Good luck and have fun.

https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space


Minimum Cost Tree From Leaf Values
Sum of Subarray Minimums
Online Stock Span
Score of Parentheses
Next Greater Element II
Next Greater Element I
Largest Rectangle in Histogram
Trapping Rain Water
```


* [`MEDIUM`][LC375 Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) 

```java
        for (int len = 2; len < n + 1; len++) {
            for (int i = 1; i <= n - len + 1; i++) { //For [i, j) => store result in dp[i, j]
                int j = i + len - 1;
                int minResult = Integer.MAX_VALUE;
                for(int k = i; k < j; k++) {
                    int result = k + Math.max(dp[i][k-1], dp[k+1][j]);
                    minResult = Math.min(minResult, result);
                }
                dp[i][j] = minResult;
            }
        }
        return dp[1][n];
    }
```

* [`HARD`][LC312 Burst Balloons](https://leetcode.com/problems/burst-balloons/)

See a [good discussion here](https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions) that covers both Remove Boxes and Burst Balloons

```java
        int[][] dp = new int[N][N];
        
        for (int len = 1; len <= N; len++) { //length of balloon array
            for (int start = 0; start <= N - len; start++) { //Interval [start, end] => dp[start][end];
                int end = start + len - 1;
                int maxResult = 0;
                //Note that k is the **last** balloon to burst in interval [start, end], so left is start-1, and right is end+1
                for (int k = start; k <= end; k++) {
                    //Don't use k-1 as left and k+1 as right!!!
                    int left = start-1 < 0 ? 1 : nums[start-1];
                    int right = end+1 == N ? 1 : nums[end+1];
                    int result = nums[k] * left * right + 
                        (k == start? 0 : dp[start][k-1]) + //Ignore the left range if k is the first one
                        (k == end ? 0 : dp[k+1][end]); //Ignore the right range if k is the last one
                    maxResult = Math.max(maxResult, result);
                }
                dp[start][end] = maxResult;
                //System.out.println("dp["+start+"]["+end+"] = " +dp[start][end]);
            }
        }
        return dp[0][N-1];
```

* [`HARD`][LC546 Remove Boxes](https://leetcode.com/problems/remove-boxes/)

```java
        for (int len = 1; len < N; len++) {
            for (int i = 0; i < N - len; i++) {
                int j = i + len;
                
                for (int count = 0; count <= i; count++) {
                    //Choice 1: remove box[i] with all adjacent box to the left
                    int choice1 = (count+1)*(count+1) + dp[i+1][j][0];
                    
                    //Choice 2: attach box[i] to box[k] of same color
                    int maxChoice2 = 0;
                    for (int k = i + 1; k <= j; k++) {
                        if (boxes[k] == boxes[i]) {
                            int choice2 = dp[i+1][k-1][0] + dp[k][j][count+1];
                            maxChoice2 = Math.max(maxChoice2, choice2);
                        }
                    }
                    dp[i][j][count] = Math.max(choice1, maxChoice2);
                }
            }
        }
        return dp[0][N-1][0];
```

* [`MEDIUM`] [LC96 Unique Binary Search Tree](https://leetcode.com/problems/unique-binary-search-trees/)
```java
        for (int len = 2; len <= n; len++) {
            int result = 0;
            for (int k = 0; k < i; k++) {
                //[0..k), k, [k+1, len)
                result += dp[k] * dp[len-1-k];
            }
            dp[i] = result;
        }
```

* TODO 
```
    
1039. Minimum Score Triangulation of Polygon Medium

1040. Minimum Cost to Merge Stones Medium
```

### Pattern 4: DP on Strings

* **Problems**: Given two *strings* s1 and s2, return some result.
* **Examples**: 
  * Two Strings: Longest Common Subsequence 
  * One String: Palindromic Substrings

#### **Template**

Most of the problems on this pattern requires a solution that can be accepted in O(n^2) complexity.

```java
// i - indexing string s1
// j - indexing string s2
for (int i = 1; i <= n; ++i) { 
   for (int j = 1; j <= m; ++j) {
       if (s1[i-1] == s2[j-1]) {
           dp[i][j] = /*code*/;
       } else {
           dp[i][j] = /*code*/;
       }
   }
}
```

Note: 
* For two strings, `i <= N` since `i` is the length of *string*
* For one string, `len < N` since len is the length of *interval*, the maximum length of interval for a string of length of N is N-1. 

If you are given one string s the approach may little vary
```java
for (int len = 1; len < n; ++len) { //Length of interval, so the max length of intervals is N-1 for string of length of N
   for (int i = 0; i < n-len; ++i) {
       int j = i + len; //Str[i, j]
       if (s[i] == s[j]) {
           dp[i][j] = /*code*/;
       } else {
           dp[i][j] = /*code*/;
       }
   }
}
```

#### Practice Questions

* [`MEDIUM`] [LC1143 Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - Two Strings Template

```java
        for (int i = 1; i <= M; i++) { //length of text1
            for (int j = 1; j <= N; j++) { //length of text2
                if (text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
```

* [`MEDIUM`] [LC647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

```java
```

* TODO - Pattern 4
```
516. Longest Palindromic Subsequence Medium

1092. Shortest Common Supersequence Medium

72. Edit Distance Hard

115. Distinct Subsequences Hard

712. Minimum ASCII Delete Sum for Two Strings Medium

5. Longest Palindromic Substring Medium
```

### Pattern 5: Making Decisions

The general problem statement for this pattern is for given situation, decide whether to use or not to use the current state. So, the problem requires you to make a decision at a current state.

* **Problems**: Given a set of values find an answer with an option to choose or ignore the current value.
* **Examples**: House Robbery, Buying and Selling Stocks
* **Approach**:
If you decide to choose the current value, use the previous result where the value was ignored; vice-versa, if you decide to ignore the current value, use previous result where value was used.


#### **Template**
```java
// i - indexing a set of values
// j - options to ignore j values
for (int i = 1; i < n; ++i) {
   for (int j = 1; j <= k; ++j) {
       dp[i][j] = max({dp[i][j], dp[i-1][j] + arr[i], dp[i-1][j-1]});
       dp[i][j-1] = max({dp[i][j-1], dp[i-1][j-1] + arr[i], arr[i]});
   }
}
```


#### Practice Questions
* [`EASY`] [198. House Robber](https://leetcode.com/problems/house-robber/)
```java
        for (int i = 1; i < N; i++) {
            dp[i][ROB] = dp[i-1][NOT_ROB] + nums[i];
            dp[i][NOT_ROB] = Math.max(dp[i-1][ROB], dp[i-1][NOT_ROB]);
        }
```


* TODO
```
121. Best Time to Buy and Sell Stock Easy

714. Best Time to Buy and Sell Stock with Transaction Fee Medium

309. Best Time to Buy and Sell Stock with Cooldown Medium

123. Best Time to Buy and Sell Stock III Hard

188. Best Time to Buy and Sell Stock IV Hard
```