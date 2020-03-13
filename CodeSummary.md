
# Code Summary

## Table of Content
- [Code Summary](#code-summary)
  - [Table of Content](#table-of-content)
- [Road Map](#road-map)
- [TODO](#todo)
    - [Java API Quick Cheat Sheet](#java-api-quick-cheat-sheet)
  - [# Basic Data Structure and Algorithm Review](#h1-id%22basic-data-structure-and-algorithm-review-9%22basic-data-structure-and-algorithm-reviewh1)
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
  - [Sorting](#sorting)
    - [Summary](#summary)
      - [Theory](#theory)
      - [Practice Question](#practice-question)
    - [Selection Sort](#selection-sort)
      - [Invariant](#invariant)
      - [Template](#template)
    - [Insertion Sort](#insertion-sort)
      - [Invaiants:](#invaiants)
      - [Template](#template-1)
      - [Properties](#properties)
    - [Merge Sort](#merge-sort)
      - [Template - MergeSort](#template---mergesort)
      - [Properties](#properties-1)
      - [Mergesort TopDown: Practical Improvements:](#mergesort-topdown-practical-improvements)
    - [Shuffle Algorithm](#shuffle-algorithm)
      - [Template: Knuth Shuffle](#template-knuth-shuffle)
    - [Quick Sort](#quick-sort)
      - [Template: Quick Sort](#template-quick-sort)
      - [Quicksort Practical Improvements](#quicksort-practical-improvements)
      - [Template: Three-Way Quick Sort](#template-three-way-quick-sort)
      - [Template: Quick Select](#template-quick-select)
    - [Heapsort and Piority Queue](#heapsort-and-piority-queue)
      - [Template: BinaryHeap](#template-binaryheap)
      - [Template: Heap Sort](#template-heap-sort)
  - [Searching](#searching)
    - [Summary](#summary-1)
      - [Equality test](#equality-test)
  - [Binary Search Tree](#binary-search-tree)
      - [Questions:](#questions)
      - [Binary Tree Traversal](#binary-tree-traversal)
      - [Binary Search Tree (BST) Operations](#binary-search-tree-bst-operations)
        - [Search](#search)
        - [Insertion](#insertion)
        - [Deletion](#deletion)
  - [Orderded Operation](#orderded-operation)
    - [BST Case Study: Intersection among geometric objects](#bst-case-study-intersection-among-geometric-objects)
    - [Range Search](#range-search)
        - [[TODO] Template: Orthogonal line segment intersection](#todo-template-orthogonal-line-segment-intersection)
    - [2-d Trees and K-d tree](#2-d-trees-and-k-d-tree)
    - [Interval Search Tree](#interval-search-tree)
    - [Rectangle Intersection](#rectangle-intersection)
- [Hash Table Review](#hash-table-review)
      - [Template: Separate Chaning Symbol Table](#template-separate-chaning-symbol-table)
      - [Template: Linear Probing Hash Symbol Table](#template-linear-probing-hash-symbol-table)
      - [Set](#set)
- [Bit Operation Review, Permutation Review](#bit-operation-review-permutation-review)
  - [Bit Cheatsheet](#bit-cheatsheet)
    - [Bit Manipulation Questions](#bit-manipulation-questions)
  - [Permutation Cheatsheet](#permutation-cheatsheet)
- [Graph Review](#graph-review)
  - [Graph - Undirected Unweighted](#graph---undirected-unweighted)
    - [Graph Traversal Summary - What BFS and DFS can do](#graph-traversal-summary---what-bfs-and-dfs-can-do)
    - [Representation](#representation)
    - [DFS](#dfs)
      - [DFS Path](#dfs-path)
      - [Connectd Components](#connectd-components)
      - [Template - Undireted Cycle](#template---undireted-cycle)
      - [Bipartite: Two-Colorability](#bipartite-two-colorability)
    - [BFS](#bfs)
      - [BFS Path - Single Source Shortest Path](#bfs-path---single-source-shortest-path)
    - [SymbolGraph](#symbolgraph)
  - [Digraph](#digraph)
    - [Digraph Search](#digraph-search)
    - [[TODO] Topological Sort](#todo-topological-sort)
    - [Strong Connected Component](#strong-connected-component)
  - [Edge-Weighted Graph](#edge-weighted-graph)
    - [Weighted Edge API](#weighted-edge-api)
    - [Minimum Spanning Tree](#minimum-spanning-tree)
      - [Template: Kruskal MST](#template-kruskal-mst)
      - [Template: Prim MST](#template-prim-mst)
  - [Edge-Weighted Digraph: Shortest Path](#edge-weighted-digraph-shortest-path)
    - [Weighted Directed Edge API](#weighted-directed-edge-api)
    - [Single Source Shortest Paths](#single-source-shortest-paths)
      - [Template: Dijkstra Shortest Path: No negative weights](#template-dijkstra-shortest-path-no-negative-weights)
      - [Tempalte: AcyclicSP: Must be DAGs, but allows for negative weights.](#tempalte-acyclicsp-must-be-dags-but-allows-for-negative-weights)
      - [Shortest paths with negative weights](#shortest-paths-with-negative-weights)
        - [Template: Bellman-Ford algorithm](#template-bellman-ford-algorithm)
        - [Template: Bellman-Form Queue Based](#template-bellman-form-queue-based)
    - [Edge-Weighted Digraph with Flow Edge: Maximum Flow](#edge-weighted-digraph-with-flow-edge-maximum-flow)
      - [Model](#model)
      - [Ford-Fulkerson Algorithm](#ford-fulkerson-algorithm)
      - [Template: Ford Fulkerson Algorithm](#template-ford-fulkerson-algorithm)
        - [Application](#application)
    - [LeetCode Examples](#leetcode-examples)
      - [DFS](#dfs-1)
        - [200 Number of Islands](#200-number-of-islands)
      - [BFS](#bfs-1)
        - [127 WordLadder](#127-wordladder)
        - [126 Word Ladder II](#126-word-ladder-ii)
- [String Review](#string-review)
  - [String Sorts](#string-sorts)
    - [Key-indexed counting demo](#key-indexed-counting-demo)
    - [LSD string (radix) sort - Least-significant-digit-first string sort](#lsd-string-radix-sort---least-significant-digit-first-string-sort)
    - [MSD string sort - Most-significant-digit-first string sort](#msd-string-sort---most-significant-digit-first-string-sort)
    - [Suffix sort](#suffix-sort)
    - [Trie](#trie)
      - [Template: R-way Trie Implementation](#template-r-way-trie-implementation)
      - [Template: Character based operations](#template-character-based-operations)
    - [Substring Search](#substring-search)
      - [Template: Knuth-Morris-Pratt DFA](#template-knuth-morris-pratt-dfa)
      - [Not Required: Boyer Moore](#not-required-boyer-moore)
      - [Not Required: Rabin-Karp](#not-required-rabin-karp)
    - [Regular Expressions](#regular-expressions)
      - [Template: NFA](#template-nfa)
      - [Application](#application-1)
      - [Java: Regular expression](#java-regular-expression)
    - [Data Compression](#data-compression)
      - [Huffman codes](#huffman-codes)
  - [Some Theory Stuff](#some-theory-stuff)
    - [Reduction](#reduction)
    - [Linear programming and Intractability](#linear-programming-and-intractability)
      - [Template: Hamilton Path - NP Complete](#template-hamilton-path---np-complete)
- [LeetCode Summary](#leetcode-summary)
  - [Sliding Window](#sliding-window)
    - [Template](#template-2)
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
      - [425 Word Square](#425-word-square)
      - [More Questions](#more-questions)
- [Compiler Template Review](#compiler-template-review)
  - [Calculator I, II, III](#calculator-i-ii-iii)
    - [High Level Design](#high-level-design)
    - [Chosen Design](#chosen-design)
- [Tree Review](#tree-review)
  - [Binary Index Tree (Fenwick Tree)](#binary-index-tree-fenwick-tree)
      - [BIT Template](#bit-template)
  - [Trie](#trie-1)
- [Dynamic Programming Review](#dynamic-programming-review)
    - [Overview](#overview)
    - [Pattern 1: Minimum Path to Reach a Target](#pattern-1-minimum-path-to-reach-a-target)
      - [**Template**](#template-3)
      - [Practice Questions](#practice-questions)
    - [Pattern 2: Distinct Ways](#pattern-2-distinct-ways)
      - [**Template**](#template-4)
      - [Practice Questions](#practice-questions-1)
    - [Pattern 3: Merging Intervals](#pattern-3-merging-intervals)
      - [**Template**](#template-5)
      - [Practice Questions](#practice-questions-2)
        - [* TODO Summarize Stacks](#ul-litodo-summarize-stacksli-ul)
    - [Pattern 4: DP on Strings](#pattern-4-dp-on-strings)
      - [**Template**](#template-6)
      - [Practice Questions](#practice-questions-3)
    - [Pattern 5: Making Decisions](#pattern-5-making-decisions)
      - [**Template**](#template-7)
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

* BFS
* DFS = preorder, inorder, postorder - using iterative approach
  * Summarize here
https://leetcode.com/problems/binary-tree-preorder-traversal/solution/

TODO 2: 
Summarize this: 
https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

TODO 3:
Review Algorithm: 
Recursion version + Iterative version for pre-order, in-order, post-order traversal, (Leetcode 545) 
Order-level traversal (Leetcode 102, 199)

~~TODO 4: Review QuickSort, QuickSelect(Leetcode 215), MergeSort~~

~~TODO 5:
Review PriorityQueue add and remove algorithm~~

TODO 6:
Review how to implement a HashMap: Hash Function + Address Conflict Resolution

Read HashSet Implementation https://leetcode.com/problems/design-hashset/solution/

~~TODO 7:
Understand Parser/Lexer etc (LeetCode 640, 536, PythonInterpreter, LeetCode Brace Expansion 1&2)~~

~~TODO 8: DP
Read Philosophy here: https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp 
Summarize Dynamic Programming Patterns: https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns~~

TODO 9: More DP
* Go through Huahua's blog: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-dp-summary/


TODO 10: All Path Generation:

* All BFS paths
  * [LC1258 Synonymous Sentences](https://leetcode.com/problems/synonymous-sentences/)
* All DFS paths

TODO 11: Monotonic Stack
* [LC496 Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
```java
//Value is monotonically decreasing from bottom to top, store value directly
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    HashMap<Integer, Integer> map = new HashMap<>(); //Element -> Next Greater Element
    Stack<Integer> stack = new Stack<>();
    
    //Build monotonic stack on nums2, only next larger element can evict current number
    for (int i = 0; i < nums2.length; i++) {
        int num = nums2[i];
        while ( !stack.isEmpty() && num > stack.peek()) {
            map.put(stack.pop(), num);
        }
        stack.push(num);
    }
    
    int[] result = new int[nums1.length];
    for (int i = 0; i < nums1.length; i++) {
        result[i] = map.getOrDefault(nums1[i], -1);
    }
    return result;
}
```
* [LC503 Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
```java
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> stack = new Stack(); //Monotonic stack of index
        int[] result = new int[nums.length];
        //First pass
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) { //Important to pop when equal to ensure monoticity
                stack.pop();
            }
            if (stack.isEmpty()) {
                result[i] = -1;
            } else {
                result[i] = nums[stack.peek()];
            }
            stack.push(i);
        }
        //Second pass for circular
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                result[i] = -1;
            } else {
                result[i] = nums[stack.peek()];
            }
            stack.push(i);
        }
        return result;
    }
```

[LC84 Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/solution/) 

```java
//Value is monotonically increasing from bottom to top, store index
//Update the square when popping
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        stack.push(-1); //Mark the end of stack
        for (int i = 0; i < heights.length; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                maxArea = Math.max(maxArea, heights[stack.pop()] * (i - stack.peek() - 1));
            }
            stack.push(i);
        }
        while (stack.peek() != -1) {
            maxArea = Math.max(maxArea, heights[stack.pop()] * (heights.length - stack.peek() - 1));
        }
        return maxArea;
    }
}
```

[LC85 Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        
        int[] histogram = new int[matrix[0].length];

        int maxArea = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                int num = matrix[i][j] - '0';
                if (num == 0) {
                    histogram[j] = 0;
                } else {
                    histogram[j] += num;
                }
            }
            maxArea = Math.max(maxArea, largestRectangleArea(histogram));
            System.out.println("Matrix area: "+maxArea);
        }
        return maxArea;
    }

    private int largestRectangleArea(int[] heights) {
        
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        stack.push(-1);
        for (int i = 0; i < heights.length; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                maxArea = Math.max(maxArea, heights[stack.pop()] * (i - stack.peek() - 1));
            }
            stack.push(i);
        }
        while (stack.peek() != -1) {
            maxArea = Math.max(maxArea, heights[stack.pop()] * (heights.length - stack.peek() - 1));
        }
        return maxArea;
    }
}
```


### Java API Quick Cheat Sheet
* Initalize list
  * Immutable: `List<Integer> list=Arrays.asList(1, 2, 3);`
  * Mutable: `List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));`
  * Mutable: `List<Integer> list = new ArrayList<>() {{add(1);}};`
* Array to List: 
  * Object Types `String[] => List<String>`: 
    ```
    List<String> result = Arrays.asList(array);
    ```
  * Primitive Types `int[] => List<Integer>`:
    ```java
    List<Integer> result = Arrays.stream(nums)
                            .boxed() //int -> Integer
                            .collect(Collectors.toList());
    ```
* List to Array: 
  * Object Types `List<String> => String[]`: 
   ```java
   String[] result = list.toArray(new String[list.size()])
   ```
  * Primitive Types `List<Integer> => int[]`:
    ```java
    int[] array = list.stream()
                        .mapToInt(i->i) //Integer -> int
                        .toArray();
    ```
* Sort array
   ```java
   int[] nums;
   Arrays.sort(nums);
   ```
* Sort list of pair
   ```java
   List<int[]> events;
   Collections.sort(events, (a,b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
   ```
* Split and rejoin string
   ```java
   String[] words = sentence.split(" ");
   words[i] = synonym;
   String newSentence = Arrays.stream(words).collect(Collectors.joining(" "));
   ```
* 2D index to 1D hash 
    ```java
    int[][] maze = new int[rows][cols]
    // {i, j} => hash
    int hash = i * cols + j;
    // hash => {1, j}
    int x = hash / cols;
    int y = hash % cols;
    ```
---
# Basic Data Structure and Algorithm Review
---

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
* [LC959 Regions Cut By Slashes ](https://leetcode.com/problems/regions-cut-by-slashes/)

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
* [MEDIUM][LC34 Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
## Sorting

### Summary

name | inplace? | stable? | best | average | worst | remarks
--|--|--|--|--|--|--
selection | Y | | $\frac{1}{2} N^2$ | $\frac{1}{2} N^2$ | $\frac{1}{2} N^2$ | n exchanges
**insertion** | Y | Y | $N$ | $\frac{1}{4} N^2$ | $\frac{1}{2} N^2$ | Best for small N or partially ordered
**merge** |  | Y | $\frac{1}{2} N lg N$ | $N lg N$ | $N lg N$ | <li>guarantee $N lg N$<br><li> stable
**quick** | Y | | $N lg N$ | $2N lg N$ | $\frac{1}{2} N^2$ | <li>probabilistic guarantee $N lg N$ <br><li>fastest in practice (less data movement than mergesort)
3-way quick | Y | | $N$ | $N lg N$ | $\frac{1}{2} N^2$ | improves quicksort for duplicated keys
**heap** | Y | | $N$ | $N lg N$ | $N lg N$ | <li>guarantee $N lg N$<br><li> in-place

* Java system sorts
  * `Arrays.sort()` uses quicksort for primitive sort for high-performance
    * Can sort differently using `Comparator` interface
    ```java
    Arrays.sort(nums);  //Sorted int[] in natural order
    Arrays.sort(nums, Collections.reverseOrder());
    ```
  * `Arrays.sort()` uses tuned mergesort for objects since extra space is likely not a concern.
    * Object implements `Comparable` interface in order to be sorted
    * Can be sorted differently with `Comparator` interface
    ```java
    Arrays.sort(employee);  //Sorted Employee[] in order implemented `compareTo` in Comparable
    Arrays.sort(employee, new EmployeeComparator()); //Sorted by `compare` defined in Comparator
    ```

#### Theory

* **Total order**: A total order is a binary relation $\le$ that satisfies:
  * **Antisymmetry**: if $v \le w$ and  $w \le v$, then $v = w$
  * **Transitivity**: if both $v \le w$ and  $w \le x$, then $v \le x$. 
    * e.g.: Rock-Paper-Scissors violates transitivity.
  * **Totality**: either $v \le w$ or  $w \le v$ or both. 
    * e.g.: Course prerequisites (topological sort) violates totality.
* `Comparable` interface requires **total order**, its motivation is to decouple the implementation datatype from the sort algorithm. It uses key within datatype to sort.

  ```java
    //Client.java
    public class PointSorter {
        public stativ void main(Point2D[] points) {
            Insertion.sort(points);
        }
    }


    //Interface.java
    pulic interface Comparable<Object> {
        public int compareTo(Object that);
    }

    //Datatype.java
    public class Point2D implements Comparable<Point2D> {
        public int compareTo(Point2D b) {
            return -1; //, or 0, or 1
        }
    }

    //Sort.java
    public static class Insertion{
        public static void sort(Comparable[] a) {
            for (int i = 1; i < a.length; i++) {
                for (int j = i; j > 0; j--) {
                    //Key point: no dependency on DataType
                    if (a[j].copmareTo(a[j-1]) < 0) {
                        swap(a, j, j-1);
                    } else {
                        break;
                    }
                }
            }
        } 
    }

  ```
* `Comparator` interface requires **total order**. It is used to sort by different field ***outside*** the datatype.   
  ```java
    //Client.java
    public class PointSorter {
        public stativ void main(Point2D[] points) {
            Arrays.sort(points, p.POLAR_ORDER);
        }
    }

    //Interface.java
    public interface Comparator<Key> {
        int compare(Key v, Key w) //Compare keys v and w
    }

    //Datatype.java
    public class Point2D {
        public final Comparator<Point2D> POLAR_ORDER = new PolarOrder;
        
        //Builtin Comparator
        privat class PloarOrder implements Comparator<Point2D> {
            public int compare(Point2D q1, Point2D q2) {
                return -1; // or 0, or 1
            }
        }
    }

  //Client.java
  Arrays.sort(points, p.POLAR_ORDER);
  ```
* **Lower bound** of compare-based sorting is $O(N log N)$. However, it may not hold if the algorithm has information about:
  * The inital order of the input
    * e.g.: Insertion sort needs only $O(N)$ compare if array is partially sorted
  * The distribution of key values
    * e.g.: Three-way quicksort needs only $O(N)$ compares if there's a constant number of distinct keys
  * The representation of the keys
    * e.g.: Radix sort requires no key compares - it accesses the data via character/digit compares

* **Stability**: preserves the relative order of items with equal keys. 
  * e.g.: Sort by name first, then sort by time next:
    *  a stable sort will preserve the order of name as well, 
    * while an unstable one will mess up the order of name. 
  * **Selection sort** is NOT stable: long distance exhange can move one equal item past equal item
  * **Insertion sort** is stable: equal items never move past each other
    * **Shell sort** is NOT stable: long distance exchange
  * **Merge sort** is stable: always takes from left subarray if equal keys. (Stability depends on the correct implementation of merge operation) 
  * **Quick sort** is NOT stable: long distance exchange during in-place partition. Use an extra array can makes partitioning easier and stable, but is not worth the cost.

#### Practice Question

* [`MEDIUM`] [LC912 Sort an Array](https://leetcode.com/problems/sort-an-array/)

  https://leetcode.com/problems/sort-an-array/discuss/276463/Java-QuickSort-%2B-SelectionSort-%2B-MergeSort-summary

```java
    public List<Integer> sortArray(int[] nums) {
        //Insertion.sort(nums);
        //Selection.sort(nums);
        //Merge.sortBU(nums);
        //Merge.sortTD(nums);
        //Quick.sort(nums);
        //Quick3Way.sort(nums);
        //Heap.sort(nums);
        return Arrays.stream(nums)
                    .boxed()
                    .collect(Collectors.toList());
    }
```

### Selection Sort
#### Invariant

* Entries to the left of `i` (including `i`) are fixed and in ascending order
* No entries to the right of `i` is smaller than any entry to the left of `i`;

#### Template
```java
    public List<Integer> sortArray(int[] nums) {
        Selection.sort(nums);
        return Arrays.stream(nums)
                    .boxed()
                    .collect(Collectors.toList());
    }
    
    public static class Selection {
        public static void sort(int[] nums) {
            int N = nums.length;
            for (int i = 0; i < N; i++) {
                int min = i; //index of min element to the right of i
                for (int j = i + 1; j < N; j++) {
                    if (nums[j] < nums[min]) { //Note: Use less comparator only
                        min = j;
                    }
                }
                swap(nums, i, min);
            }
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

* $\sim N^2/2$ compares and $N$ exchanges
* Running time insensitive to input, even if the input is sorted. 
* Data movement is minimal. Linear number of exchanges.

### Insertion Sort

#### Invaiants:
* Entries to the left of `i` (including `i`) are in ascending order
* Entries to the right of `i` have not been seen yet.

#### Template
```java
    public static class Insertion {
        public static void sort(int[] nums) {
            int N = nums.length;
            for (int i = 1; i < N; i++) {
                for (int j = i; j > 0; j--) {
                    if (nums[j] < nums[j-1]) { //Note: Use less comparator only
                        swap(nums, j, j-1);
                    } else {
                        break;
                    }
                }
            }
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

#### Properties
* **Average Case**: For randomly-ordered with distinct keys,  $\sim N^2/4$ compares and $\sim N^2/4$ exchanges on average
* **Best case**: If the array is in ascending order, insertion sort makes $N-1$ compares and $0$ exchange.
* **Worst case**: If the array is in descending order, insertion sort makes $\sim N^2/2$ compares and $\sim N^2/2$ exchanges 
* Important Proposition: For **partially-sorted** arrays, insertion sort runs in **linear** time.
  * Concept
    * Inversion: A pair of keys that are out of order
    * Partially sorted array: number of inversions is $\le cN$ (linear)
  * Proof
    * Number of inversions equals number of exchanges. 
    * Number of compares = exchanges + (N - 1)

### Merge Sort

#### Template - MergeSort 

```java
    public static class Merge {
        public static void sortBU(int[] nums) {
            int N = nums.length;
            int[] aux = new int[N];
            for (int size = 1; size < N; size = size * 2) {
                for (int low = 0; low < N - size; low += size * 2) {
                    int mid = low + size - 1;
                    int high = low + size + size - 1;
                    merge(nums, aux, low, mid, Math.min(high, N-1));
                }
            } 
        }
        
        public static void sortTD(int[] nums) {
            int[] aux = new int[nums.length];
            sort(nums, aux, 0, nums.length-1);
        }
    
        //Helper function for sortTopDown
        private static void sort(int[] nums, int[] aux, int low, int high) {
            /* //--Unoptimized---
            if (high <= low) {
                //Array of length 1
                return;
            }
            */
            
            //OPTIMIZATION 1: insertion for small array
            int CUTOFF = 7;
            if (high <= low + CUTOFF - 1) {
                Insertion.sort(nums, low, high);
                return;
            }

            int mid = low + (high - low)/2;
            sort(nums, aux, low, mid);
            sort(nums, aux, mid+1, high);
            
            //OPTIMIZATION 2: no merge if two arrays are already sorted
            if (nums[mid] <= nums[mid+1]) {
                return;
            }
            
            merge(nums, aux, low, mid, high);
        }
    
        //Shared between TopDown and BottomUp approach
        //stably merge A1 = nums[low..mid] and A2 = nums[mid+1..high] using aux[low..high]
        private static void merge(int[] nums, int[] aux, int low, int mid, int high) {
            //Copy to aux[] - use as readonly copy once initialized
            for (int k = low; k <= high; k++) {
                aux[k] = nums[k];
            }

            // Merge back to nums[]
            //i iterates in [low..mid], j iterates in [mid+1..high]
            int i = low, j = mid+1;
            for (int k = low; k <= high; k++) {
                if (i > mid) { //A1 is done
                    nums[k] = aux[j++]; 
                } else if ( j > high) { //A2 is done
                    nums[k] = aux[i++]; 
                } else if (aux[j] < aux[i]) { //NOTE: use values in aux array to compare!!!
                    nums[k] = aux[j++];
                } else { //Use A2
                    nums[k] = aux[i++];
                }
            }
        }
    }
```


#### Properties

* [GOOD] Time Complexity:  $O(N log N)$
* [OKAY] Space Complexity: $O(N)$
* [GOOD] Mergesort is stable


#### Mergesort TopDown: Practical Improvements:
* [Easy to do] Use insertion sort for small already. Cutoff is usually around 7  
* [Easy to do] Stop if already sorted.
* [Tricky to implement] Eliminate the copy to the auxiliary array.


### Shuffle Algorithm

* **Goal**: Rearrange array so that result is a uniformly random permutation in $O(N)$ instead of $O(N log N)$

* **PracticeQuestion**  
  * [LC384 Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/)

* **Shuffle Sort**: Naive approach
  * Generate a random real number for each array entry, and then sort the array. 
  * Bounded by $O(N log N)$ sort algorithm.

#### Template: Knuth Shuffle
* This is a $O(N)$ uniform shuffling algorithm.
* Note: `j` must be chosen between `[0, i]`. An easy WRONG implementation is to choose between [0, nums.length-1] all the time, but this will not be an uniform distribution anymore.

```java
    public static class KnuthShuffle {
        public static void shuffle(int[] nums) {
            for (int i = 1; i < nums.length; i++) {
                int j = new Random().nextInt(i+1); //NOTE: between [0, i]. Not [0, N]. Otherwise not uniform
                swap(nums, i, j);
            }
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

NOTE: What happens if interger is chosen between `0` and `N-1` instead of `0` to `i`? It will not be unifromely random.

### Quick Sort

Important: Partition Strategy with Duplicated Keys
* [BAD] Don't stop on equal keys. $\sim N^2 / 2$ compares when all keys equal
  * NOTE: Must stop scans on equal keys, otherwise quicksort will take $O(N^2)$ time, even with random shuffle
* [GOOD] Stop on equal keys. $\sim N log N$ compares when all keys equal => quicksort
* [BETTER] Put all equal keys in place. $\sim N$ compares when all keys equal => 3-way quick sort


#### Template: Quick Sort 
```java
    public static class Quick {
        public static void sort(int[] nums) {
            KnuthShuffle.shuffle(nums);
            sort(nums, 0, nums.length - 1);
        }
        
        //Invariant: low < high
        private static void sort(int[] nums, int low, int high) {
            if (low >= high) {
                //Length <= 1
                return;
            }
            
            //j is in correct place after partition
            int j = partition(nums, low, high);
            sort(nums, low, j-1);
            sort(nums, j+1, high);
        } 
        
        
        //VERY TRICKY to implement correctly.
        //nums[low] is used as pivot
        //Invariant: low + 1 <= i < j <= high. 
        private static int partition(int[] nums, int low, int high) {
            int pivot = nums[low];
            int i = low, j = high + 1;//Set boundary like this since we are using ++i instead of i++
            while (true) {
                //Find first i within bound that's not less than a[low]
                //NOTE: If not using self-increment here, will not be able to proceed when nums[i] == nums[j] == pivot
                //NOTE: Use ++i instead of i++ here, otherwise, the index being compared here will not be the one used in swap
                while (nums[++i] < pivot) { 
                    if (i == high) { //i is already rightmost
                        break;
                    }
                }
                
                //Find first j from right within bound that's not greater than a[low]
                while (pivot < nums[--j]) {
                    if (j == low) { //j is already Leftmost 
                        break;
                    }
                }
                
                //Swap i, j if not crossed
                if (i >= j) {
                    break;
                }
                swap(nums, i, j);
            }
            //Put pivot elemnt in place, everything to the right of j is greater.
            swap(nums, low, j);
            return j;
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

#### Quicksort Practical Improvements
* [Easy to do] Use insertion sort for small already. Cutoff is usually around 7  
* [Easy to do] Use a median-of-3 as the pivot element, instead of always `nums[low]`
  ```java
    private static void sort(int[] nums, int low, int high) {
        //OPTIMIZATION 1: insertion for small array
        int CUTOFF = 7;
        if (high <= low + CUTOFF - 1) {
            Insertion.sort(nums, low, high);
            return;
        }
        //OPTIMIZATION 2: Median of 3
        int median = medianOf3(nums, low, low + (high-low)/2, high);
        swap(nums, low, median);
        //Original
        int j = partition(nums, low, high);
        sort(nums, low, j-1);
        sort(nums, j+1, high);
    } 
  ```

#### Template: Three-Way Quick Sort

Practice Question: [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

**Time Complexity**
* O(N) when constant number of keys 
* O(N log N) probalistic gurantee after shuffle 
* O(N^2) worst case if not shuffle

**Invariant** 
* smaller than pivot: [low, lt)
* larger than pivot: (gt, high]
* i examins [lt, gt]

```java
    //Invariant: 
    //  * smaller than pivot: [low, lt)
    //  * larger than pivot: (gt, high]
    //  * i examins [lt, gt]
    // O(N) when constant number of keys, O(N log N) probalistic gurantee after shuffle, O(N^2) worst case if not shuffle
    public static class Quick3Way {
        public static void sort(int[] nums) {
            sort(nums, 0, nums.length - 1);
        }
        
        private static void sort(int[] nums, int low, int high) {
            if (high <= low) {
                return;
            }
            
            int pivot = nums[low];
            int lt = low, gt = high;
            
            int i = low; 
            while (i <= gt) {
                if (nums[i] < pivot) {
                    swap(nums, i++, lt++);
                } else if (nums[i] > pivot) {
                    //Why not use for loop? Because i is not self-increment here
                    swap(nums, i, gt--); 
                } else {
                    //If equal, do nothing
                    i++;
                }
            }
            
            sort(nums, low, lt - 1);
            sort(nums, gt + 1, high);
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

#### Template: Quick Select
Average Case: O(N). Worst Case: $O(N^2)$, but this is extremely unlikely after Random Shuffle.

* Practice Question: [LC215 Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

```java
    public static class Quick {
        //Select K-th element: Average O(N)
        public static int select(int nums[], int K) {
            //NOTE: very important to probabillistic guarantee performance
            KnuthShuff.shuffle(nums);
            //Similar to binary search
            int low = 0, high = nums.length - 1;
            while (low < high) {
                int j = partition(nums, low, high);
                if (j < K) {
                    low = j + 1;
                } else if (j > K) {
                    high = j -1;
                } else {
                    return nums[K];
                }
            }
            return nums[K];
        }
        
        //VERY TRICKY to implement correctly. Exactly the same implementation as quicksort
        //Invariant: low + 1 <= i < j <= high
        //j will be in-place after partition
        private static int partition(int[] nums, int low, int high) {
            int pivot = nums[low];
            int i = low, j = high+1; //Init like this since we will pre-increment.
            while (true) {
                //Use pre-increment so that comparison and swap index are the same
                while (nums[++i] < pivot) {
                    if (i == high) { //i is at rightmost position
                        break;
                    }
                }
                
                while (pivot < nums[--j]) {
                    if (j == low) { //j is leftmost position
                        break;
                    }
                }
                
                //swap if i and j haven't crossed
                if (i >= j) { //Invariant i < j;
                    break;
                }             
                swap(nums, i, j);
            }
            //j is the first element that is not greater than pivot
            //Swap with pivot element
            swap(nums, low, j);
            return j;
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
```

### Heapsort and Piority Queue

#### Template: BinaryHeap

* PriorityQueue is a data type, hiwch can be implemented as ordered array, or unordered array, or binary heap. 


* Binary heap is an array representation of a hep-ordered complete binary tree.
  * Heap-ordered binary tree
    * Key in nodes
    * Parent's key no smaller than children's keys.
  * Array representation: 
    * indices start at 1
    * Takes nodes in **level** order
    * No explicit links needed. 
* Properties
  * Largest key is `a[1]`, which is the root of the binary tree
  * Parent of node at k is `k/2`
  * Children of node at k are `2k` and `2k+1` 


* NOTE: The key must be immutable! Otherwise how can you tell the order is correct? That's why we can't use PriorityQueue<int[2]> in java, since the content might change.

```java
PriorityQueue<Integer> minPQ = new PriorityQueue<Integer>();
PriorityQueue<Integer> maxPQ = new PriorityQueue<Integer>(Collections.reverseOrder());
```

* Note: The way of initializing minPQ and maxPQ is applicable to any Object implements `Comparable`, not just `Integer` :-D

**Practice Questions**:
* [MaxHeap] [LC1046 Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
* [MinHeap] [LC703 Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)
* [`MEDIUM`][LC378 Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix) [`Key Design Point: One Poll should be associated with at most one Offer`]
* [`MEDIUM`][LC373 Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) [`Key Design Point: One Poll should be associated with at most one Offer`]
* [`MEDIUM`][LC313 Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) [`Key Design Point: One Poll should be associated with at most one Offer`]
* [`MEDIUM`][LC264 Ugly Number II][https://leetcode.com/problems/ugly-number-ii/submissions/]
* [`MEDIUM`][LC1054 Distance Barcodes](https://leetcode.com/problems/distant-barcodes)

```java
    public class MaxPQ<Key extends Comparable<Key>> {
        private Key[] heap;
        private int n; //Index of last valid Key

        public MaxPQ(int capacity) {
            //PQ is 1-based index
            heap = (Key[]) new Comparable[capacity+1];
        }
        
        public void insert(Key key) {
            n++;
            heap[n] = key; //Put x at the end of array
            swim(n); //Swim x up
        }
        
        public Key removeMax() {
            Key max = heap[1];
            swap(1, n);
            heap[n] = null; //Avoid loitering
            n--; //Must decrease before sink, since sink will use this to check boundary
            sink(1);
            return max;
        }

        private void swim(int i) {
            //Parent of i is i/2
            while (i > 1 && less(i/2, i)) {
                swap(i, i/2);
                i = i/2;
            }
        }

        private void sink(int i) {
            //Children of i is 2*i and 2*i+1
            while (2 * i <= n) { //have at least one child
                int j = 2*i; //j is left child
                if (j < n && less(j, j+1)) {//if right child exist and is larger
                    j = j+1; //j is right child
                }
                //Heap order holds, then break
                if (!less(i, j)) {
                    break;
                }
                swap(i, j);
                i = j;
            }
        }

        private void swap(int i, int j) {
            Key temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }

        private boolean less(int i, int j) {
            return heap[i].compareTo(heap[j]) < 0;
        }
    }
```

#### Template: Heap Sort

* Heap construction is $O(N)$. It uses $\le 2N$ compares and exchanes
* Heap sort is $O(N lg N)$. It uses $\le 2N lg(N)$ compares and exchanes

Significant: In-place with NlogN **worst** case
 * Mergesort: No. Linear extra space. (In-place possible, but not practical)
 * Quicksort: No. Quadratic worst case (N log N worst-case possible, but not practical)
 * Heapsort: YES.

Property: Heap is optimal for bothe time and space
  * inner loop longer than quicksort
  * make poor use of cache
  * not stable

```java
    //index-0 is not used during heapsort. nums[1..nums.length-1] will be heapsorted
    public static class Heap {
        public static void sort(int[] nums) {
            int n = nums.length - 1;
            //Heap construct O(N)
            for (int k = n/2; k >= 1; k--) {
                sink(nums, k, n);
            }
            //Keep finding the largest and put to back O(N lg N)
            while (n > 1) {
                swap(nums, 1, n); //Put largest in place
                sink(nums, 1, --n); //Recreate heap order
            }

            //Put a[0] back to place - O(N) - insertion sort 
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] > nums[i+1]) {
                    swap(nums, i+1, i);
                } else {
                    break;
                }
            }
        }

        //Sink index i to maintain heap order in [1..n]
        private static void sink(int[] nums, int i, int n) {
            while (2 * i <= n) {
                int child = 2 * i;
                if (child < n && nums[child] < nums[child+1]) {
                    child = child + 1;
                }
                if (nums[i] >= nums[child]) { //Already in place
                    break;
                }
                swap(nums, i, child);
                i = child;
            }
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    
```

## Searching

### Summary

name | search | insert | delete | ordered ops? | key interface | comment
--|--|--|--|--|--|--
sequential search (unordered list) | $N$ | $N$ | $N$ | | `equals()` | 
binary search (ordered array) | $lg N$ | $N$ | $N$ | Y | `compareTo()` | 
BST | guarantee $N$ <br>average $1.39lgN$ | guarantee $N$ <br>average $1.39lgN$ | guarantee $N$ <br>average $\sqrt{N}$ | Y | `compareTo()` |
Balanced BST | $lgN$ | $lgN$ | $lgN$ | Y | `compareTo()` | <li>2-3 tree<br><li>red-black tree<br><li>b-tree<br><li>Fenwick tree
Separate Chaning | guarantee N<br>average 3-5 | guarantee N<br>average 3-5  | guarantee N<br>average 3-5  | | `equals()`<br>`compareTo()` | constant under uniform hashing assumption
Linear Probing | guarantee N<br>average 3-5 | guarantee N<br>average 3-5  | guarantee N<br>average 3-5  | | `equals()`<br>`compareTo()` | constant under uniform hashing assumption

Ordered operations:
* search, insert/delete, min/max, floor/ceiling, select, ordered iteration

SymbolTable[KEY] = VALUE

VALUE: Any generic type
KEY: type
* Assume kesy are `Comparable`, use `compareTo()`
* Asume keys are any generic type, use `equals()` to test equality
* Assume keys are any generic type, use `equals()` to test equality; use `hashCode()` to scramble key.

#### Equality test

Java requirement: For any reference x, y, and z
* Equivalence relation must hold
    * Reflexive: `x.equals(x)` is `true`
    * Symmetric: `x.equals(y)` if and only if `y.equals(x)`
    * Transitive: if `x.equals(y)` and `y.equals(z)`, then `x.equals(z)`
* Not-null: `x.equals(null)` is `false`


All java cleasses inherit a method `equals()`
* Default implementation: `x == y`, whether x and y refer to the same object
* User-defined implementation
  * Typical Wrong Way: Only checking all significant fields are the same.
    ```java
    public class Date implements Comparable<Date> {
        private final int month;
        private final int day;
        private final int year;

        public boolean equals(Date that) {
            //Checking all significant fields are the same.
            if (this.day != that.day) return false;
            if (this.month != that.month) return false;
            if (this.year != that.year) return false;
            return true;
        }
    }
    ```
  * Good Template for implementing equals
  ```java
  //NOTE1: use final keyword. Typically unsafe to use equal with inheritance (would violates symmetry)
  public final class Date implements Comparable<Date> {
        private final int month;
        private final int day;
        private final int year;

        //NOTE2: compare with Object, not Date. Why? Experts still debate
        public boolean equals(Object y) {
            //NOTE3: Optimize for true object equality 
            if (y == this) return true;
            //NOTE4: Not-null requirements
            if (y == null) return false;
            //NOTE5: Objects must be in the same class. Religion: getClass() vs instanceof()
            if (y.getClass() != this.getClass()) return false;

            //NOTE6: cast is guarantee to succeed
            Date that = (Date) y;

            //Checking all significant fields are the same.
            if (this.day != that.day) return false;
            if (this.month != that.month) return false;
            if (this.year != that.year) return false;
            return true;
        }
    }
  ```
  
Recipe for comparing fields
* if field is primitive, use `==`
  * Unless if it's `double`, use `Double.compare()`, otherwise need to deal with `-0.0` and `NaN`
* if field is an object, use `equals()`
  * e.g.: `String`
* If field is an array, apply to each entry, or `Arrays.deepEquals(a,b)`. Don't use `a.equals(b)`

## Binary Search Tree

A Binary Search Tree(BST) is a binary tree in **symmetric order**.

* **Symmetric order**: each node has a key, and every node's key is
  * Larger than all keys in its left subtree
  * Smaller than all keys in its right subtree

NOTE: where as binary heap is a binary tree in **heap order**

* Assume no duplicate key, there is a 1-1 correspondence between a BST and quicksort. Think root of BST as the partition element for quicksort

* Tree Traversal
  * BFS: level
  * DFS: preorder, postorder, inorder
    * Implementation: Recursion, Iterative with Stack, Morris Traversal using O(1) space

#### Questions:

#### Binary Tree Traversal
* [LC94 Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)
* [LC144 Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)
  * [LC589 N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
* [LC145 Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)
  * [LC590 N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
  * [LC114 Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) - Postorder (Right, Left, Root)
* [LC102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)
  * [LC103 Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)
  * [LC107 Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
  * [LC116 Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
* [LC105 Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
* [LC106 Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
* [LC889 Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal)

#### Binary Search Tree (BST) Operations
##### Search
* [LC700 Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)
```java
class Solution {
    //Recursiont
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) {
            return root;
        } 
        return val < root.val ?
           searchBST(root.left, val):
           searchBST(root.right, val);
    }
}
```
```java
class Solution {
    //Iterative
    public TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (val < root.val) {
                root = root.left;
            } else if (val > root.val) {
                root = root.right;
            } else {
                return root;
            }
        }
        return null;
    }
}
```

##### Insertion
* [LC701 Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)
```java
    //Recursion
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }        
        if (root.val < val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }
        return root;
    }
```

##### Deletion
* [LC450 Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst)
```java
    private int successor(TreeNode root) {
        root = root.right;
        while (root.left != null) {
            root = root.left;
        }
        return root.val;
    }
    
    private int predecessor(TreeNode root) {
        root = root.left;
        while (root.right != null) {
            root = root.right;
        }
        return root.val;
    }
    
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        
        //delte from the right subtree
        if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else {
            //Base Case 1: leaf, then delete by setting null
            if (root.left == null && root.right == null) {
                root = null;
            } else if (root.right != null) {
                //Case 2: Has a right child, put successor value here, and delete successor in right tree
                root.val = successor(root);
                root.right = deleteNode(root.right, root.val);
            } else {
                //Case 3: Has a left child, put predecessor value here, and delete predecessor in right tree
                root.val = predecessor(root);
                root.left = deleteNode(root.left, root.val);
            }
            
        }
        return root;
    }
```
* [LC270 Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value)
```java
    public int closestValue(TreeNode root, double target) {
        int closestVal = root.val;
        TreeNode node = root;
        while (node != null) {
            if (Math.abs(node.val - target) < Math.abs(closestVal - target)) {
                closestVal = node.val;
            }
            node = target < node.val ? node.left : node.right;
        }
        return closestVal;
    }
```
* [LC272 Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii)
* [LC230 Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
  * Recursive Inorder - O(N)
```java
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> nums = inorder(root, new ArrayList<Integer>());
        return nums.get(k-1);
    }
    
    private List<Integer> inorder(TreeNode node, List<Integer> list) {
        if (node == null) {
            return list;
        }
        
        inorder(node.left, list);
        list.add(node.val);
        inorder(node.right, list);
        return list;
    }
```
  * Iterative Inorder - O(H)
```java
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        while (true) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            k--;
            if ( k == 0) {
                return root.val;
            }
            root = root.right;
        }
    }
```

## Orderded Operation

* min: leftmost node
* max: rightmost node
* ceiling: smallest key $\ge$ given key
* floor: largest value $\le$ given key
```java
private TreeNode floor(TreeNode root, key) {
    if (x == null) {
        return null;
    }

    if (key == root.key) {
        return root;
    } else if(key < root.key) {
        return floor(root.left, key);
    }

    //If floor is not in right tree, then it is current root
    TreeNode node = floor(root.right, key);
    if (node != null) {
        return node;
    } else {
        return root;
    }
}
```
* size:

```java
//Add count field to TreeNode
private class Node {
    private Key key;
    private Value val;
    private TreeNode left;
    private TreeNode right;
    private int count; //This field will help with `size`, `rank` and `select`
}
//Update count everytime during put
private TreeNode put(Node root, Key key, Value val) {
    if (x == null) {
        return new Node(key, val, 1);
    }

    if (key < root.key) {
        root.left = put(root.left, key, val);
    } else if (key > 0) {
        key.right = put(root.right, key, val);
    } else {
        root.val = val;
    }
    root.count = 1 + size(root.left) + size(root.right);
    return root;
}
//Return size
private int size() {
    return root == null ? 0 : root.count;
}
```
* rank: How many keys < k?
```java
public int rank(TreeNode root, Key key) {
    if (x == null) {
        return 0;
    }

    if (key < root.key) {
        return rank(root.left, key);
    } else if (key > root.key) {
        return 1 + size(root.left) + rank(root.right, key);
    } else {
        return size(root.left);
    }
}
```
* Iteration/Traversal:
   * Inorder, preorder, postorder
 

NOTES:

* 2-3 tree 
  * allows 2-node (one key, two children) and 3-node (two keys, three children)
  * Properties:
    * Symmetric order: Inorder traversal yields keys in ascending order
    * Perfectly balanced: every path from root to null lnk has same length
  * Tree hight:
    * Worst case: lg N (all 2-nodes)
    * Height = 12 ~ 20 for million nodes
    * Height = 18 ~ 30 for billion nodes
* Left-learning red black BST is a concise implmentation to 2-3 tree
  * Model: Hard to maitain 2-3 node, so we use a RED link to glue two 2-nodes to one 3-nodes, where the larger key is the root
    * Trivia: Why call it Red-black tree? Sedgewick first discovered algorithm, laser color printing was pretty new, and RED seems to popout among all colors.
  * Properties: 1-1 correspondence between 2-3 tree and LLRB
    * No node has two red links (No 4-node)
    * Equal number of black links from root to null (Black are real links, red are internal glue of 3-node)
    * Red links lean left (visualize red link as horizontal to see as 2-3 node)
  * Implementation:
    * Search: exact the same as regular BST, since no color information is required 
    * Basic Util for LLRB
        * Left rotaion: orient a (temprorily) right-learning red link to lean left. Useful for `node.right = RED` [Not left leaning]
        * Right rotation: Orient a left-learning red link to (temproraily) lean right. Useful for `node.left = RED` and `node.left.left = RED` [Two left RED links in a row.]
        * Color flip: recolor to split a (temporary) 4 node. Useful for `node.left = RED` and `node.right = RED` [ 4-node]
    * Insertion:
      * Always insert with a RED link, then restore the properties by left rotate, right rotate and color flip
      ```java
      private Node put(Node h, Key key, Value val) {
        //LLBR: create RED by default
        if (h == null) return new Node(key, val, RED);

        //Regular BST put
        if (key < root.key) {
            h.left = put(h.left, key, val);
        } else if (key > root.key) {
            h.right = put(h.right, key, val);
        } else {
            h.val = val;
        }

        //LLBR: order matters here
        if (isRed(h.right) && !isRed(h.left)) {
            h = rotateLeft(h);
        } 
        if (isRed(h.left) && isRed(h.left.left)) {
            h = rotateRight(h);
        }
        if (isRed(h.left) && isRed(h.right)) {
            flipColors(h);
        }

        return h;
      }

      ```
* B-tree is a generalization of 2-3 tree
  * Properties:
    * Root have at least 2 links
    * All other nodes have at least M/2 links (half full), and at most M-1 links (ful)
 * B tree of order M with N keys requires $log_{M-1}N$ and $log_{M/2}N$ probes. 
   * `In practise, the number of probes is at most 4`. (e.g.: When N = 62 billion and M = 1024 $log_{M-1}N \lt 4$)
   * Optimization: always keep root page in memory

### BST Case Study: Intersection among geometric objects

### Range Search
* Application: Database find all keys between k1 an k2

* Geometric Interpretation: keys are point on a line. Find/count points in a given 1d interval

##### [TODO] Template: Orthogonal line segment intersection
  * Sweep-line algorithm:
  Sweep vertical line from left to right
    * x-coordinate define events
    * horizontal-segment (left endpoint): insert y-coordinate into BST
    * horizontal-segment (right endpoint): delete y-coordinate from BST
    * vertical-segment: range search for interval of y-endpoint
  * Significance: Reduce 2d orthogonal line segment intersection search to 1 d range search

TODO: add leetcode questions
* [986 Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
* [56 Merge Intervals](https://leetcode.com/problems/merge-intervals/)
* [218 The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
*  [`Hard`][LC759 Employee Free Time](https://leetcode.com/problems/employee-free-time/)
### 2-d Trees and K-d tree

* 2d tree is an extension of BST allow us to process set of points in space. Keys are 2d now  
* Naive Implementation: using grid
  * Choose $\sqrt N$ as M for good time-space trade off
  * Space: $M^2 + N$
  * Time: $1 + N/M^2$
  * Problem: Clustering
  * How to addres? Adapt to density
* Sapce-partition trees: 
 * 2d tree: tree represents horizontal or vertial separation
 * quadtree
* Use Case:
  * Seach point lies in a rectangle
  * Nearest neighbor search
* K-d tree: represents points in k-dimension
  * Use Case: N-body simulation
  
 TODO:
 * [558 Quad Tree Intersection](https://leetcode.com/problems/quad-tree-intersection/)
 
### Interval Search Tree
Interval search tree
 * Use left endpoint as BST key
 * Store max endpoint in subtree rooted at node 

To insert an interval (lo, hi)
  * Insert into BST, using lo as the key
  * Update max in each node on search path

To search for any one interval that intersects query interval (lo, hi)
  * If interval in node intersects query interval, return it
  * Else if left subtree is null, go right
  * Else if max endpoint in left subtree is less than lo, go right
  * Else go left

### Rectangle Intersection
* Driving Motivation: Early 1970, microprocessor design became a geometric problem. O(NlogN) algorithm is required to maintain Moore's law
* Algorithm: Sweep line algorithm => reduce to interval search problem
  * Left endpoint: interval search for y-interval of rectangle; insert y-interval


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


#### Template: Separate Chaning Symbol Table
```java
public class SeparateChaningHashST<Key, Value> {
    private int M = 97;
    private Node[] st = new Node[M];

    private static class Node {
        private Object key;
        private Object val;
        private Node next;
    }

    private int hash(Key key) {
        //Hashcode is between -2^31 to 2^31-1, we need positive array index
        //Need to and with 0x7ffffff instead of Math.abs(hashCode),
        //otherwise Math.abs(-2^31) will still be -2^31. 
        return (key.hashCode() & 0x7fffffff) % M);
    }

    public Value get(Key key) {
        int i = hash(key);
        for (Node x = st[i]; x != null; x = x.next) {
            if (key.equals(x.key)) {
                return (Value) x.val;
            }
        }
        return null;
    }

    public void put(Key key, Value val) {
        int i = hash(key);
        for (Node x = st[i]; x != null; x = x.next) {
            if (key.equals(x.key)) {
                x.val = val;
                return;
            }
        }
        st[i] = new Node(key, val, st[i]);
    }
}
```

#### Template: Linear Probing Hash Symbol Table
```java
public class LinearProbingHashST<Key, Value> {
    private int M = 30001;
    private Value[] vals = (Value[]) new Object[M];
    private key[] key = (Key[]) new Object[M];

    private int hash(Key key) {
        return (key.hashCode() & 0x7fffffff) % M;
    }

    public void put(Key key, Value val) {
        int i;
        for (i = hash(key); keys[i] != null; i = (i+1) % M) {
            if (keys[i].equals(key)) {
                break;
            }
        }
        keys[i] = key;
        vals[i] = val;
    }

    public int get(Key key) {
        for (int i = hash(key); keys[i] != null; i = (i+1) % M) {
            if (key.equals(keys[i])) {
                return vals[i];
            }
        }
        return null;
    }
}
```

* Separate Chaining - typical key size:  M ~ N/4
  * Easier to implement delete
  * Performance degrades gracefully
  * Clustering less sensitive to poorly designed hash function
* Linear Probing - typical key size: M ~ N/2
  * Less Wasted space
  * Better cache performance

* Two-probe hashing (Separate-chaining variant)
  * Hash to two positions, insert key in shorter of the two chains
  * Reduces expceted length of longest chain to $log log N$
* Double hashing (linear probing variant)
  * Use linear probing, but skip a variable amount, not just 1
  * Effectively elimnates clustring, can allo table to become nearly full
  * More difficult to implement delete;
* Cuckoo hashing (linear probing variant): 
  * Hash key to two positions; insert key to either position; if occupied, reinsert displaced key into its alternative position (and recur)
  * Constant worst case time for search

#### Set
[TreeSet API][LC220 Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)



# Bit Operation Review, Permutation Review

## Bit Cheatsheet
Bitwise note

* `num | (1<<k)`: set num's k-th bit as 1
* `num & (1<<k)`: get num's k-th bit
* `num ^ (1<<k)`: flip num's k-th bit
  * See Leetcode 1066 Campus Bike II
* `index & (-index)`: get lowest set bit (useful for Fenwick Tree)
* `x &= (x-1)`: Set Last set bit(rightmost set bit) to 0. 
  * See LC338 Counting Bits Solution 4
  * See LC191 Number of 1 bits
* `i & 1`: same as `i % 2`, but faster
  * See LC338 Counting Bits Solution 3


### Bit Manipulation Questions
* [`MEDIUM`][LC751 IP to CIDR](https://leetcode.com/problems/ip-to-cidr/)

## Permutation Cheatsheet
* Read this: https://leetcode.com/problems/permutation-sequence/solution/


# Graph Review 
Four major types of graph
Representation of the graph and the processing of the graph should be separated

* Graph - Undirected Unweighted 
  * DFS - Connectivity - O(V+E)
    * DFS Path - Single Source Path
    * CC - Connected Components
    * Cycle Detection - acyclic
    * Two Colorability - bipartite
  * BFS - Shortest - O(V+E)
    * BFS Path - Single Source Shortest Path
  * SymbolGraph
* DiGraph - Directed Unweighted
  * DirectedDFS - O(V+E)
  * Topological Sort - Reverse Post DFS Order on a DAG
    * DirectedCycle
    * DepthFirstOrder
      * Preorder, postorder, reverseposorder
  * Strong Connected Digragh - Kosaraju's SCC - DFS of Digraph in reverse post order of the Digraph reverse
  * All Pair Reachability - TransitiveClosure - Run DirectedDFS on all vertex
* EdgeWeightedGraph - Undirected Weighted
  * Minimum Spanning Trees - O(E log E)
    * Prim's algorithm: keep one connected piece, till all nodes reached - DFS + PQ of edge
    * Kruskal's algorithm: keep adding small edges, till all nodes reached - UF + PQ of edge
* EdgeWeightedDigraph - Directed Digraph
  * Shortest Path
    * Dijkstra's algorithm: inviting the closest person among all club members into the club
  * General Shortest Path Algorithm
    * Bellman-Ford
  * Network Flow
    * Ford Fulkerson shortest-augmenting path maxflow algorithm

## Graph - Undirected Unweighted

### Graph Traversal Summary - What BFS and DFS can do

Problem | Description | BFS | DFS | time 
--|--|--|--|--
s-t path | Is there a path between s and t? | Y | Y | $E + V$ 
shortest s-t path | What is the shortest path between s and t? | Y |  | $E + V$ 
connected component | are any of two nodes connected | Y | Y | $E + V$
biconnected component  | two-color |   | Y | $E + V$ 
cycle | Is there a cycle in the graph? | Y | Y | $E + V$ 
Euler cycle | Is there a cycle that uses each edge exactly once? [Yes. If all even degree] | | Y | $E + V$ 
Hamilton cycle (Traveling Salesman Problem) | Is there a cycle that uses each vertex exactly once? (Intractable problem) |  |  | $2^V$ 
biconnectivity | Is there vertext whose removal disconnects the graph? |
planarity | can the graph be drawn in the plane with no corssing edges? (Hire an expert) | | Y | $E + V$
graph isomorphism | Do two adjacency lists represent the same graph? (No one knows) |  |  | $2^{\sqrt{N log N}}$ 

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

Goal: Find all vertices connected to v

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
* Find the connected components of a graph.
a.k.a: Divide vertices into equivalence class

* Compare to Union-Find:
  * Union-Find is more interactive, whereas graph is processing all the unions, then ask for find.
  * Union-Find is $O(\alpha(N))$ whereas Connected Component is O(1)


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

#### Template - [Undireted Cycle](https://algs4.cs.princeton.edu/41graph/Cycle.java.html)
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
    private void dfs(Graph G, int v, int parent) {
        marked[v] = true;
        for (int w: G.adj(v)) {
            if (!marked[w]) {
                dfs(G, w, v);
            } else if (w != parent) {
               // The (marked[w] && parent != w) means, the node w has been visited, but not because it's the parent that's passed in from the previous recursion, so that it means it has a cycle.
               hasCycle = true; 
            }
        }
    }
}
```

* [`MEDIUM`][LC261 Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)


#### Bipartite: Two-Colorability
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

* [`MEDIUM`][LC785 Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

### BFS
* **Idea** :
    Maitainig a queue of all vertices that are *marked* but whose *adjacency lists haven not been checked*
        => Mark first, then put in the queue
* **Algorithm** :
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

## Digraph
Problem:
* Path: Is there a directed path form s to t?
* Shortest Path: What is the shorted directed path form s to t?
* Topological Sort: Can you draw a digraph that all points upward?
* Strong Connected Component: Is there a directed path between all pairs of vertices?

### Digraph Search

* ***Reachability**: Find all vertices reachable form s along a directed path
  * Solution: Directed DFS
    * Same methods as for undirected graphs. 
    * DFS is a **digraph** algorithm,
    * Every undirected graph is a digraph (with edges in both directions)
  * Use Case
    * Program Control-flow analysis. Remove dead code block.
    * Mark-sweep garbage collector in java
* **Shorted Path**
 * Solution: Directed BFS
    * Same methods as for undirected graphs. 
    * BFS is a **digraph** algorithm,
    * Every undirected graph is a digraph (with edges in both directions)
  *  **Multiple-source shorted Path**: Put the set of source vertices in the queue, and do BFS. 


### [TODO] Topological Sort
TODO-Summarize both BFS and DFS approach

* DFS Order: 
  * **Preorder**: Put the vertex on a `queue` **before** the recursive calls.
  * **Postorder**: Put the vertex on a `queue` **after** the recursive calls.
  * **Reverse postorder**: Put the vertex on a `stack` **after** the recursive calls.

* Reverse DFS postoder of a DAG is a topological order
* Note: need to check for Cycle first
```java
public class DepthFirstOrder {
    private boolean[] marked;
    private Queue<Integer> preorder = new Queue<Integer>();
    private Queue<Integer> postorder = new Queue<Integer>();
    private Stack<Integer> reversePost; 

    public DepthFirstOrder(Digraph G) {
        reversePost = new Stack<Integer>();
        marked = new boolean[G.V()];
        for (int v = 0; v < G.V(); v++) {
            if (!makred[v]) {
                dfs(G, v);
            }
        }
    }

    private void dfs(Digraph G, int v) {
        marked[v] = true;
        preorer.enqueue(v);
        for (int w: G.adj(v)) {
            if (!makred[w]) {
                dfs(G, w);
            }
        }
        postorder.enqueue(v);
        reversePost.push(v);
    }

    public Iterable<Integer> topologicalOrder {
        return reversePostorder;
    }
    
    public Iterable<Integer> reversePostorder() {
        return reversePostorder;
    }
}
```

```java
public class DirectedCycle {
    private boolean[] marked;        // marked[v] = has vertex v been marked?
    private int[] edgeTo;            // edgeTo[v] = previous vertex on path to v
    private boolean[] onStack;       // onStack[v] = is vertex on the stack?
    private Stack<Integer> cycle;    // directed cycle (or null if no such cycle)


    public DirectedCycle(Digraph G) {
        marked  = new boolean[G.V()];
        onStack = new boolean[G.V()];
        edgeTo  = new int[G.V()];
        for (int v = 0; v < G.V(); v++)
            if (!marked[v] && cycle == null) {
                dfs(G, v);
            }
    }

    // check that algorithm computes either the topological order or finds a directed cycle
    private void dfs(Digraph G, int v) {
        onStack[v] = true;
        marked[v] = true;
        for (int w : G.adj(v)) {

            // short circuit if directed cycle found
            if (cycle != null) return;

            // found new vertex, so recur
            else if (!marked[w]) {
                edgeTo[w] = v;
                dfs(G, w);
            }

            // trace back directed cycle
            else if (onStack[w]) {
                cycle = new Stack<Integer>();
                for (int x = v; x != w; x = edgeTo[x]) {
                    cycle.push(x);
                }
                cycle.push(w);
                cycle.push(v);
                assert check();
            }
        }
        onStack[v] = false;
    }

    public boolean hasCycle() {
        return cycle != null;
    }

    public Iterable<Integer> cycle() {
        return cycle;
    }
}
```

* [`MEDIUM`][LC207 Course Schedule](https://leetcode.com/problems/course-schedule/)
* [`MEDIUM`][LC210 Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

### Strong Connected Component
* Problem: Is there a directed path between all paris of vertices.
  * Preprocess in linear time, and query in constant time.
* Idea: Run DFS on the graph, consider unvisited vertex using the topological order of its reverse Graph. (instead of vertex number in regular DFS)
  * Only two line differences 
  * Reverse Graph: Strong components in $G$ are the same as in its reverse Graph $G^R$
  * Kernel: Contract each strong component into a single vertex

```java
public class KosarajuSharirSCC {
    private boolean[] marked;     // marked[v] = has vertex v been visited?
    private int[] id;             // id[v] = id of strong component containing v
    private int count;            // number of strongly-connected components

    /**
     * Computes the strong components of the digraph {@code G}.
     * @param G the digraph
     */
    public KosarajuSharirSCC(Digraph G) {

        // run DFS on G, using reverse postorder to guide calculation
        marked = new boolean[G.V()];
        id = new int[G.V()];

        // compute reverse postorder of reverse graph
        DepthFirstOrder dfs = new DepthFirstOrder(G.reverse()); //DIFF 1: Compute reversePostorder of reverse graph
        for (int v : dfs.reversePost()) { //DIFF 2: Visit in reverPostorder
            if (!marked[v]) {
                dfs(G, v);
                count++;
            }
        }
    }

    // DFS on graph G
    private void dfs(Digraph G, int v) { 
        marked[v] = true;
        id[v] = count;
        for (int w : G.adj(v)) {
            if (!marked[w]) dfs(G, w);
        }
    }

    //Number of strong component
    public int count() {
        return count;
    }

    public boolean stronglyConnected(int v, int w) {
        return id[v] == id[w];
    }
}
```


## Edge-Weighted Graph

### Weighted Edge API
```java
public class Edge implements Comparable<Edge> {
    private final int v, w;
    private final double weight;

    public Edge(int v, int w, double weight) {
        this.v = v;
        this.w =w;
        this.weight = weight;
    }

    public int either() {
        return v;
    }

    public int other(int vertex) {
        return vertex == v? w : v;
    }

    public int compareTo(Edge that) {
        if (this.weight < that.weight) {
            return -1;
        } else if (this.weight > that.weight) {
            return 1;
        } else {
            return 0;
        }
    }
}

public class EdgeWeighedGraph {
    private final int V;
    privatee final Bag<Edge>[] adj;

    public EdgeWeightedGraph(int V) {
        this.V = V;
        adj = (Bag<Edge>[]) new Bag[V];
        for (int v = 0; v < V; v++>) {
            adj[v] = new Bag<Edge>();
        } 
    }

    public void addEdge(Edge e) {
        int v = e.either(), w = e.other(v);
        adj[v].add(e);
        adj[w].add(e);
    }

    public Iterable<Edge> adj(int v) {
        return adj[v];
    }
}

```

### Minimum Spanning Tree

Given: Undirected graph G with **positive** edge weights (connected)

#### Template: Kruskal MST

Time Complexity: $O(ElogE)$ (building PQ takes $O(E)$, and delMin takes $O(logE)$)
```java
public class KruskalMST {
    private Queue<Edge> mst = new Queue<Edge>();

    public KruskalMST(EdgeWeightedGraph G) {
        MinPQ<Edge> pq = new MinPQ<Edge>();
        for (Edge e: G.edges()){
            pq.insert(e);
        }

        UF uf = new UF(G.V());
        while (!pq.isEmpty() && mst.size() < G.V() - 1) {
            Edge e = pq.delMin();
            int v = e.either(), w = e.other(v);
            if ( !uf.connected(v, w)) {
                uf.union(v, w);
                mst.enqueue(e);
            }
        }
    }

    public Iterable<Edge> edges() {
        return mst;
    }
}
```

#### Template: Prim MST
Time Complexity: $O(ElogE)$ (building PQ takes $O(E)$, and delMin takes $O(logE)$)
```java
public class LazyPrimMST {
    private boolean[] marked;
    privaet Queue<Edge> mst; //MST edges
    private MinPQ<Edge> pq; //PQ of edges

    public LazyPrimMST(WeightedEdgeGraph G) {
        pq = new MinPQ<Edge>();
        mst = new Queue<Edge>();
        marked = new boolean[G.V()];
        visit(G, 0);

        while ( !pq.isEmpty() && mst.size() < G.V() - 1) {
            Edge e = pq.delMin();
            int v = e.either();
            int w = e.other(v);
            if (marked[v] && marked[w]) { //Both endpoints already in T
                continue;
            }
            mst.enqueue(e);
            if ( !marked[v] ) visit(G, v);
            if ( !marked[w] ) visit(G, w);
        }
    } 

    private void visit(WeightedGraph G, int v) {
        marked[v] = true;
        for (Edgge e: G.adj(v)) {
            if (!marked[e.other(v)]) {
                pq.insert(e);
            }
        }
    }

    public Iterable<Edge> mst() {
        return mst;
    }
}
```

## Edge-Weighted Digraph: Shortest Path 


algorithm | restriction | typical case | worst case | extra space
--|--|--|--|--
topological sort | no directed cycles | E + V | E + V | V
Dijkstra (binary heap) | no negative weight | E log V | E log V | V
Bellman-Form (naive) | no negative cycles | EV | EV | V
Bellman-Ford (queue-based) | no negative cycles | E + V | EV | V

Note: 
* Directed cycles make the problem harder
* Negative weights make the problem harder
* Negative cycles makes the problem intractable


Problems
* [`MEDIUM`][787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

### Weighted Directed Edge API
```java
public class DirectedEdge implements Comparable<Edge> {
    private final int v, w;
    private final double weight;

    public Edge(int v, int w, double weight) {
        this.v = v;
        this.w =w;
        this.weight = weight;
    }

    public int from() {
        return v;
    }

    public int to() {
        return w;
    }

    public int compareTo(Edge that) {
        if (this.weight < that.weight) {
            return -1;
        } else if (this.weight > that.weight) {
            return 1;
        } else {
            return 0;
        }
    }
}

public class EdgeWeighedDigraph {
    private final int V;
    privatee final Bag<DirectedEdge>[] adj;

    public EdgeWeightedGraph(int V) {
        this.V = V;
        adj = (Bag<Edge>[]) new Bag[V];
        for (int v = 0; v < V; v++>) {
            adj[v] = new Bag<DirectedEdge>();
        } 
    }

    public void addEdge(DirectedEdge e) {
        int v = e.from();
        adj[v].add(e);
    }

    public Iterable<DirectedEdge> adj(int v) {
        return adj[v];
    }
}
```

### Single Source Shortest Paths

* Generic algorithm 
  * Initialize distTo[s] = 0 and distTo[v] = INF for all other vertices
  * Repeat until optimality condition are satisfied
    * Relax any edge
    ```java
    private void relax(DirectedEdge e) {
        int v = e.from(), w = e.to();
        if (distTo[w] > distTo[v] + e.weight()) { //Cheaper to go to w from v, then update
            distTo[w] = distTo[v] + e.weight();
            edgeTo[w] = e;
        }
    }
    ```

* Efficient implementation: How to choose which edge to relax?
  * Dijkstra's algorithm (nonnegative weights): 
    * consider vertices by distance to source
  * Topological sort algorithm (no directed cycles): 
    * consider vertices in topological order
    * holds true even if there is negative cycle
  * Bellman-Ford algorithm (no negative cycle)

#### Template: Dijkstra Shortest Path: No negative weights
```java
public class DijkstraSP {
    private DirectedEdge[] edgeTo;
    priate double[] distTo;
    private IndexMinPQ<Duble> pq;

    public DijkstraSP(EdgeWeightedDigraph G, int s) {
        edgeTo = new DirectedEdge[G.V()];
        distTo = new double[G.V()];

        pq = new IndexMinPQ<Double>(G.V());

        for (int v = 0; v < G.V(); v++) {
            distTo[v] = Double.POSITIVE_INFINITY;
        }
        distTo[s] = 0.0;

        pq.insert(s, 0.0); 
        while (!pq.isEmpty()) {
            int v = pq.delMin();
            for (DirectedEdge e: G.adj(v)) {
                relax(e);
            }
        }
    }

    private void relax(DirectedEdge e) {
        int v = e.from(), w = e.to();
        if (distTo[w] > distTo[v] + e.weight()) { //Cheaper to go to w from v, then update
            distTo[w] = distTo[v] + e.weight();
            edgeTo[w] = e;
            //Update PQ
            if (pq.contains(w)) {
                pq.decreaseKey(w, distTo[w]); //Decrease the value associated with w to distTo[w]
            } else {
                pq.insert(w, distTo[w]);
            }
        }
    }
}
```

Note: Dijkstra's is essentially the same as Prim's algorithm, both computing a graph's **spanning tree**
  * Prim's: Closest vertex to the **tree** (via an undirected edge)
  * Dijkstra's: Closest vertex to the **source** (via a directed path)


* Problems
  * [`MEDIUM`][LC505 The Maze II](https://leetcode.com/problems/the-maze-ii/) 
  ```java
      
    private boolean isValid(int x, int y) {
        return x >= 0 && x < rows && y >= 0 && y < cols && maze[x][y] == 0;
    }
    
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        this.maze = maze;
        this.rows = maze.length;
        this.cols = maze[0].length;
        //We mark a node as settled after dequeue, instead of mark as visited when enqueue
        boolean[] settled = new boolean[rows * cols];
        
        int source = hash(start);
        int target = hash(destination);
        
        // (1D coordinate, cost) pair
        int POS = 0, COST = 1;
        PriorityQueue<int[]> minPQ = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[COST], o2[COST]));
        minPQ.offer(new int[] {source, 0});
        
        while (!minPQ.isEmpty()) {
            //Dijkstra algorithm: the time we pop some element from the PQ, we are guaranteed to find the minimum path cost to it
            //Trick: We mark a node as visited only when we dequeue, instead of enqueue, therefore, there is same cell associated with different cost in the heap. Alternatively, we could use Indexed PQ
            int[] current = minPQ.poll();
            settled[current[POS]] = true;
            if (current[POS] == target) {
                return current[COST];
            }
            
            //For all directed weighted edge, relax and put on queue
            int row = current[POS] / cols, col = current[POS] % cols;
            for (int[] dir: DIRS) {
                //Compute neighbor (x, y, cost)
                int x = row, y = col, cost = 0;
                while (isValid(x + dir[DX], y + dir[DY])) {
                    x += dir[DX];
                    y += dir[DY];
                    cost++;
                }
                // Didn't move at all, invalid neighbor
                if (cost == 0) {
                    continue;
                } 
                int neighbor = hash(x, y);
                if (!settled[neighbor]) {
                    minPQ.offer(new int[]{neighbor, current[COST] + cost});
                }
            }  
        }
        return -1;
    }
  ```

#### Tempalte: AcyclicSP: Must be DAGs, but allows for negative weights.

```java
    public AcyclicSP(EdgeWeightedDigraph G, int s) {
        edgeTo = new DirectedEdge[G.V()];
        distTo = new double[G.V()];

        for (int v = 0; v < G.V(); v++) {
            distTo[v] = Double.POSITIVE_INFINITY;
        }
        distTo[s] = 0.0;

        Topological topological = new Topological(G); //Topological order
        for (int v: topological.order()) {
            for (DirectedEdge e: G.adj(v)) {
                relax(e);
            }
        }
    }
```

Applications:  
* Context-aware resizing
* Longest Paths in edg-weighted DAG <=> equivalent: reverse sens of equality in relax()
  * Negate all weights
  * Find shortest paths
  * Negate weights in result
* Parallel Job scheduling: 
  * Model each job as START, END node with DURATION as edge
  * Model job dependency as 0 weight edge
  * Find the longest path form the source to schedule each job

#### Shortest paths with negative weights

* Dijkstra: doesn't work with negative edge weights. Re-weighting doesn't work either, because you penalize the path for being too long
* Acyclic assume there is no directed cycle.

##### Template: Bellman-Ford algorithm
* Note: We relax the edge **V times**. Compare to Dijkstra that only relax the edge **once**, that's why Dijkstra cannot find shortest path that's longer (but with negative weight). 
* Note: Bellman-Form assumes no negative cycle, otherwise you just keep looping in the negative cycle, and make the path however short you want.

```java
for (int i = 0; i < G.V(); i++> {
    for (int v = 0; v < G.V(); v++) {
        for (DirectedEdge e: G.adj(v)) {
            relax(e);
        }
    }
})
```
* If some vertex still updates, it means v is part of negative cycle.
  * Application: Arbitrage oppurunity for foreign currency exchange rates
    * Vertex = currency
    * Edge = transaction, with weight equal to exchange to rate
    * Find a directed cycle whose product of edge weights is > 1 
    *    => take `-ln(x)` to make `product > 1` to `sum < 0`

##### Template: Bellman-Form Queue Based

TODO

### Edge-Weighted Digraph with Flow Edge: Maximum Flow

#### Model 
* Input: A weighted diagram, source vertex s, and target vertex t
* Mincut: Find a cut of minimum capacity (how do we cut the graph efficiently, with a minimal amount fo work)
* Maxflow: Find a flow of maximum value (what's the maximum amount of stuff that we can get through a graph)

#### Ford-Fulkerson Algorithm
 ```
 start with 0 flow
 while there exists an augmenting path:
   - find an augmenting path
   - compute bottleneck capacity
   - increase flow on that path by bottleneck capacity
 ```

 Questions:
 * How to compute a mincut: Easy
 * How to find an augmenting path: BFS works well
 * If FF terminates, does it always compute a maxflow: Yes, see theorem
 * Does FF always terminate? Yes, if capacities are intergers (or augmenting paths are chosen carefully) 
 * If so, after how many augmentations? requires clever analysis

 Theorem
  * Augmenting path theorem: A flow f is a maxflow if and only if no augmenting paths
  * Maxflow-mincut theorem: value of the maxflow = capacity of mincut

FF Performance depends on choice of augmenting paths

augmenting path | number of paths | implementation
--|--|--
shortest path | <= 1/2 EV | queue (BFS)
fattest path | <= E ln(EU) | priority queue
randome path | <= EU | randomized queue
DFS path | <= EU | stack (DFS)

U is the max integer capacity

#### Template: Ford Fulkerson Algorithm
* Concept
  * Residual (spare) capacity:
    * Forward edge: residual capcity = `c - f`
    * Backward edge: redidual capcity = `f`
  * Augment flow
    * Forward edge: add delta
    * Backward edge: subtract delta

```java
public class FlowEdge {
    private final int v, w; //From and to
    private final double capacity; //maximum capacity
    private double flow; //NOTE: it is mutable

    public FlowEdge(int v, int w, double capacity) {
        this.v = v;
        this.w = w;
        this.capacity = capacity;
    }

    public int from() { return v; }
    public int to() {return w;}
    public double capacity() {return capacity;}
    public double flow() {return flow;}
    public int other(int vertex) {
        if (vertext == v) {return w;}
        else if (vertext == w) {return v;}
        else throw new RuntimeException("Illegal Endpoint");
    }

    public double residualCapacityTo(int vertex) {
        if (vertext == v) {return flow;} //backward edge: w -> v
        else if (vertext == w) {return capacity - flow;} //forward edge: v -> w
        else throw new RuntimeException("Illegal Endpoint");
    } 

    public void addResidualFlowTo(int vertex, double delta) {
        if (vertext == v) {return flow -= delta;} //backward edge: w -> v
        else if (vertext == w) {return flow += delta;} //forward edge: v -> w
        else throw new RuntimeException("Illegal Endpoint");
    }
}

public class FlowNetwork {
    private final int V;
    private Bag<FlowEdge>[] adj;

    public FlowNetwork(int V) {
        this.V = V;
        adj = (Bag<FlowEdge>[]) new Bag[V];
        for (int v = 0; v < V; v++) {
            adj[v] = new Bag<FlowEdge>();
        }
    }

    public void addEdge(FlowEdge e) {
        int v = e.from();
        int w = e.to();
        adj[v].add(e);
        adj[w].add(e);
    }

    public Iterable<FloEdge> adj(int v) {
        return adj[v];
    }
}

public class FordFulkerson {
    private boolean[] marked; //true if s->v path in residual network
    private FlowEdge[] edgeTo; //Last edge on s-> v path
    private double value; //value of flow
    public FordFulkerson(FlowNetwork G, int s, int t) {
        value = 0.0;
        while (hasAugmentingPath(G, s, t)) {
            double bottleneck = Double.POSITIVE_INFINITY;
            //Compute bottleneck capcity
            for (int v = t; v != s; v = edgeTo[v].other(v)) {
                bottleneck = Math.min(bottleneck, edgeTo[v].redidualCapcityTo(v));
            }
            //Augmentflow
            for (int v = t; v != s; v = edgeTo[v].other(v)) {
                edgeTo[v].addResidualFlowTo(v, bottleneck);
            }
            value += bottleneck;
        }
    }

    //Finding a shortest augmenting path (BFS)
    private boolean hasAugmentingPath(FlowNetwork G, int s, int t) {
        edgeTo = new FlowEge[G.V()];
        marked = new boolean[G.V()];

        Queue<Integer> = new Queue<Integer>();
        queue.enqueue(s);
        marked[s] = true;
        while (!queue.isEmpty()) {
            int v = queue.dequeue();
            for (FlowEdge e: G.adj(v)) {
                int w = e.other(v);
                if (!marked[w] && (e.residualCapacityTo(w) > 0)) {
                    edgeTo[w] = e;
                    marked[w] = true;
                    queue.enqueu(w);
                }
            }
        }
        return marked[t];
    }

    //Max flow / Min Cut value
    public double value() {
        return value;
    }

    //Is v reachable from s in residual network
    public boolean inCut(int v) {
        return marked[v];
    }
}

```

##### Application

* Bipartite matching problem
    * Each student has several offer, and each company sends offer to different student
    * Q: can each student get a job?
* Baseball elimination
    * Which teams have a chance of finishing the season with most wins?


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

# String Review
## String Sorts
### Key-indexed counting demo

* Goal: Sort an array a[] of N integers between 0 to R-1
* Solution: Four steps [Why not just count and recompute? Because we might want to move associated information as well, so key-indexed counting is more general]

* NOTE: this is a stable sort
```java
int N = a.length;
int[] count = new int[R+1];

//Step 1: count frequenceis of each ltter using key as index 
for (int i = 0; i < N; i++) {
    count[a[i] + 1]++; //IMPORTANT: offset by 1, computing the rightside bound of a[i]
}

//Step 2: compute frequency cumulates which specify desitnations
for (int r = 0; r < R; r++) {
    count[r+1] += count[r];
}

//Step 3: access cumulte using key as index to move items
for (int i = 0; i < N; i++) {
    aux[count[a[i]]++] = a[i];
}

//Step 4: move back to original array
for (int i = 0; i < N; i++) {
    a[i] = aux[i];
}
```

### LSD string (radix) sort - Least-significant-digit-first string sort
NOTE: String must be same length. Sort from right to left

### MSD string sort - Most-significant-digit-first string sort
NOTE: support different length, similar to quicksort

### Suffix sort

Application: keyword-in-context searrch: suffix-sorting solution
* Preprocess: suffix sort the text
* Query: binary search for query; scan until mismatch

Application: longest repeasted substring
* Q: Given a string of N characters, find the longest repeated substring

### Trie
* Trie is faster than Hash for String key, since it does not need to examine the entire key
* Random Fact: Trie is the middle part of "retrieval", but we pronounce as "try" to distinguish from "tree"

#### Template: R-way Trie Implementation

```java

public class TrieST<Value> {
    private static final int R = 256; //Extended ASCII
    private Node root = new Node();

    private static class Node {
        private Object value;
        private Node[] next = new Node[R];
    }

    public void put(String key, Value val) {
        root = put(root, key, val, 0);
    }

    private Node put(Node x, String key, Value val, int d) {
        if (x ==  null) {
            x = new Node();
        }
        if (d == key.length()) {
            x.val = val;
            return x;
        }
        char c = key.charAt(d);
        x.next[c] = put(x.next[c], key, val, d+1);
        return x;
    }

    public boolean contains(String key) {
        return get(key) != null;
    }

    public Value get(String key) {
        Node x = get(root, key, 0);
        if (x == null) {
            return null;
        }
        return (Value) x.val;
    }

    private Node get(Node x, String key, int d) {
        if (x == null) {
            return null;
        }
        if (d == key.length()) {
            return x;
        }
        char c = key.charAt(d);
        return get(x.next[c], key, d+1);
    }
}
```

* Improvement:
  * Ternary Search Trie: instead of having R children, only have three children: left, middle, right
  * TST with R2: first 2 level with 26 ways, lower levels do TST

#### Template: Character based operations

```java
public class TrieST<Value> {
    //API: All keys: inorder traversal
    Iterable<String> keys() {
        Queue<String> queue = new Queue<String>();
        inorder(root, "", queue);
        return queue;
    }

    private void collect(Node x, String prefix, Queue<String> q) {
        if (x == null) {
            return;
        }
        if (x.val != null) {
            q.enqueue(prefix);
        }
        for (char c = 0; c < R; c++) {
            inorder(x.next[c], prefix + c, q);
        }
    }

    //API: Prefix Match: autocomplete
    public Iterable<String> keysWithPrefix(String prefix) {
        Queue<String> queue = new Queue<String>();
        Node x = get(root, prefix, 0); //root of subtrie for all strings begining with given prefix
        collect(x, prefix, queue);
        return queue;
    }

    //API: Find longest key insymbol table that is a preix of query string
    public String longestPrefixOf(String query) {
        int length = search(root, query, 0, 0);
        return query.substring(0, length);
    }

    // keep track of longest key encountered so far
    private int search(Node x, String query, int d, int length) {
        if (x == null) {
            return length;
        }
        if (x.val != null) {
            length = d;
        }
        if (d == query.length()) {
            return length;
        }
        char c = query.charAt(d);
        return search(x.next[c], query, d+1, length);
    }
}
```

### Substring Search

#### Template: Knuth-Morris-Pratt DFA

Q: What's the interpretation of DFA state after reading in `txt[i]`?
A: State = number of characters in pattern that have been matched.

```java
//i is text[i] to look at, and j is the state
public int search(String txt) {
    int i, j, N = text.length(); 
    for (i = 0, j = 0; i < N && j < M; i++) {
        j = dfa[txt.charAt(i)][j];
    }
    if (j == M) {
        return i - M;
    } else {
        return N;
    }
}
```

How to build DFA?
* For each state j:
    * Copy `dfa[][X]` to `dfa[][j]` for mismatch case
    * Set `dfa[pat.charAt(j)][j]` to `j+1` for match case
    * Update X

```java
public KMP(String pat) {
    this.pat = pat;
    M = pat.length();
    dfa = new int[R][M];
    dfa[pat.charAt(0)][0] = 1;

    int X = 0;
    for (int j = 1; j < M; j++) {
        for (int c = 0; c < R; c++) { //Copy mismatch case from restart state
            dfa[c][j] = dfa[c][X];
        }
        dfa[pat.charAt(j)][j] = j+1; //Set match case
        X = dfa[pat.charAt(j)][X]; //Update restart state
    }
}
```

Analysis
* Proposition: KMP substring search accesses no more than M + N chars to search for a pattern of length M in a text of length N
* Proposition: KMP constructs dfa[][] in time and space proportional to RM

#### Not Required: Boyer Moore

KMP needs O(MN) space, we want to reduce the space complexity to O(M)

How about let's match the pattern from the right to left?
Then we can skip lots of characters.

Q: How much to skip?
A: Precompute index of rightmost occurence of character c in pattern (-1 if character not in pattern)

```java
right = new int[R];
for (int c = 0; c < R; c++) {
    right[c] = -1;
}
for (int j = 0; j < M; j++) {
    right[pat.charAt(j)] = j;
}
```

```java
public int search(String txt) {
    int N = txt.length();
    int M = pat.length();
    int skip;
    for (int i = 0; i <= N-M; i+= skip) {
        skip = 0;
        for (int j = M-1; j >= 0; j--) {
            if (pat.charAt(j) != txt.charAt(i+j)) {
                skip = Math.max(1, //in case other term is nonpositive
                        j - right[txt.charAt(i+j)]); //compute skip value
                break;
            }
        }
        if (skip == 0) {
            return i; //match
        }
    }
} 
```

* Property: Mismatched heuristics takes about ~N/M character compares
* Worst Case: Can be as bad as MN

#### Not Required: Rabin-Karp

* Basic Idea = modular hashing
  * Compute a hash of pat[0..M-1];
  * For each i, compute a hash of txt[i..M+i-1]
  * If pattern hash = text substring hash, check for a match

```
(a + b) mod Q = ( (a mod Q) + (b mod Q) )mod Q
(a * b) mod Q = ( (a mod Q) * (b mod Q) )mod Q
```

### Regular Expressions

* Note:
  * Kleen Theorem: there is a one to one mapping between Regular Expression and DFA
  * However, to implement DFA for RE for guaranteed linear time, we might have exponential state. Therefore, we will use NFA instead, which runs in quandrantic time for worst case, and linear for average case.

* Q: How to determine whether a string is matched by an automaton?
  * DFA: Deterministic => easy because exactly one applicable transition
  * NFA: Nondeterministic => can be several applicable transition; need to select the right one.
* Q: How to simulate NFA?
  * Systematically consider all possible transition sequnces

* NFA representation:
  * State names: Integer from 0 to M, where M is number of symbols in RE
  * Match-transition: keep regular expression in array `re[]`
  * epsilon-transition: store in a diagraph G
* Q: How to efficiently simulate NFA?
  * Maintaining set of **all** possible transition that NFA could be in after reading in the firs i text characers.
* Diagraph reachability: final all vertices reahbale from a given source or **set** of vertices
  * solution: run DFS from each source, without unmarking vertices
* How to build an NFA?
  * `CLOSURE`: three epsilon transition edges for each `*` operator
  * `OR`: Add two epsilon transition edges for each `|`
* Goal: Write a program to build the epsilon transition digarph.    
  * Challenges: 
     * remeber left parenthese `(` to implement CLOSURE and OR; 
     * remember `|` to implement
  * Solution:
    * `(`: push onto stack
    * `|`: push onto stacck
    * `)`: pop corresponding `(` and possibly intervening `|`, add epsilon transition edge for CLOSURE/OR

#### Template: NFA
* NFA simulation: N-character text is recognized by the NFA corresponding to an M-character pattern takes time proporationl to MN in worst case.

```java
public class NFA {
    private cahr[] re; //match transitions
    private Digraph G; //epsilon transition diagraph
    private int M;     //number of states

    public NFA(String regexp) {
        M = regexp.length();
        re = regexp.toCharArray();
        G = buildEpsilonTransitionDigraph();
    }

    //O(MN) for worst case
    public boolean recogize(String txt) {
        Bag<Integer> pc = new Bag<Integer>(); //Program Counter: set of all interger that NFA could be in
        DirectedDFS dfs = new DirectedDFS(G, 0); //Compute states reachable from start by epsilon transtion
        for (int v = 0; v < G.V(); v++) { 
            if (dfs.marked(v)) {
                pc.add(v);
            }
        }

        for (int i = 0; i < txt.length(); i++) {
            //compute state reachable after sanning past txt.charAt(i);
            Bag<Integer> match = new Bag<Integer>();
            for (int v: pc) {
                if (v == M) {
                    continue;  //Nothing to do if in final state
                }
                if ((re[v] == txt.charAt(i)) || re[v] == '.') {
                    match.add(v+1);
                }
            }

            //follow epsilon transiton
            dfs = new DirectedDFS(G, match);
            pc = new Bag<Integer>();
            for (int v = 0; v < G.V(); v++) {
                if (dfs.marked(v)) {
                    pc.add(v);
                }
            }
        }

        //After scanning, accept if can end in state M
        for (int v: pc) {
            if (v == M) {
                return true;
            }
        }
        return false;
    }

    //Parsing the regex
    public Digraph buildEpsilonTranstionDigraph() {
        Digraph G = new Digraph(M+1);
        Stack<Integer> ops = new Stack<Integer>(); //Index of ops
        for (int i = 0; i < M; i++) {
            int lp = i; //left parentheses

            //Handle OR
            if (re[i] == '(' || re[i] == '|') {
                ops.push(i);
            } else if (re[i] == ')') {
                int or = ops.pop();
                if (re[or] == '|') {
                    lp = ops.pop();
                    G.addEdge(lp, or+1);
                    G.addEdge(or, i);
                } else {
                    lp = or;
                }
            }

            //Handle CLOSURE, look 1 char ahead
            if (i < M-1 && re[i+1] == '*') { 
                G.addEdge(lp, i+1);
                G.addEdge(i+1, lp);
            }

            //Add next transition
            if (re[i] == '(' || re[i] == '*' || re[i] == ')') {
                G.addEdge(i, i+1);
            }
        }
        return G;
    }


}
```

#### Application

* Grep

Time Complexity: Worst case O(MN), which is the same as brute force substring match
```java
public class GREP  {
    public static void main(String[] args) {
        String regexp = "(.*" + args[0] + ".*)";
        NFA nfa = new NFA(regex);
        while (StdIn.hasNextLine()) {
            String line = StdIn.readLine();
            if (nfa.recognizes(line)) {
                StdOut.println(line);
            }
        }
    }
}
```

#### Java: Regular expression

* Pattern 1 - Validate Check

Q: Does the iput match the regex?

```java
String regex = args[0];
String input = args[1];
System.out.println(input.matches(re));
```

Pattern 2 - Havesting information

Goal: Print all substrings of input that match a RE

```java
String input = in.readAll();
Pattern pattern = Pattern.compile(regex); //compile() creates a NFA
Matcher matcher = pattern.matcher(input); //matcher() creates a NFA simulator
while (matcher.find()) { //find() looks for the next match
    StdOut.println(matcher.group()); //group() gives substring most recently found by find()
}
```

WARNING: Typical ipmlementation, including java, grep, python, do **NOT** guarantee performance like we did.

e.g.: regex = `(a|aa)*b` and input=`aaaaaaaaaaaaaaac`, add few more `a` and observe the exponential growth.

### Data Compression

* Motivation: 
  * Save **space** when storiing
  * Save **time** when transmitting it
* Algorithm:
  * Run Length Encoding
  * Huffman compression: fixed-length symbol with variable-length code
    * How to avoid ambiguity? Ensure that no codeword is a prefix of another.
      * e.g.: Fixed Length Code; Append special stop char; Use prefix-free code
  * LZW compression: variable-length symbol with fixed-length code
    * Progressively learn and update model as you read character

#### Huffman codes
* Q: How to find best prefix-free code? 
* A: Huffman algorithm:
  * Count frequency for each char in input
  * Stat with one node corresponding to each char i (with weigth freq[i])
  * Repeat until single trie formed:
    - select two tries with min weight freq[i] and freq[j]
    - merge into single trie with weigth freq[i] and frq[j]

```java
private static Node buildTrie(int[] freq) {
    MinPQ<Node> pq = new MinPQ<Node>();
    for (char i = 0; i < R; i++) {
        if(freq[i] > 0) {
            pq.insert(new Node(i, freq[i], null, null));
        }
    }

    while(pq.size() > 1) {
        Node x = pq.delMin();
        Node y = pq.delMin();
        Node parent = new Node('\0', x.freq+y.freq, x, y);
        pq.insert(parent);
    }
    return pq.delMin();
}
```

## Some Theory Stuff

* Topics
  * Reduction: Design algorithms, establish lower bounds, classify problems
  * Linear programming: the ultimate practical problem solving model
  * Intractability: problems beyond our reach

### Reduction

* Definition: Problem X reduces to probem Y if you can use an algorithm that solves Y to help solve X
* Design Algorithm: given algorithm for Y, can also solve X.
* Classify Problems
  complexity | order of growth | example
  --|--|--
  linear | N | min, max, median
  linearithmic | N log N | sorting, convex hull
  M(N) | ? | integer multiplication, division, square root...
  MM(N) | ? | matrix multiplication, Ax = b, least suare ,determinant
  ... | .. | ...
  NP-complete | probably not N^b | SAT, IND-SET, ILP

### Linear programming and Intractability

* Q: Which alogrihtm are usfeful in practice? 
   * A: Those with poly-time algorithm O(aN^b), instead of O(2^N), O(N!)
   * Intractable: A problem is intractable if it can't be solved in polynomial time
* Q: which algorithm have polytime?
   * : Hard to tell
* Q: Four fundamental problems - do they have polytime solution
  * LSOLVE: given a system of **linear equations**, find a solution (variables are real)
    * Yes, Gaussian eliination
  * LP: given a system of **linear inequalities**, find a solution (variables are real)
    * Yes, ellipsoid algorithm can help solve it, but it was open question for years.
  * ILP: given a system of **linear inequalities**, find a 0-1 solution (variables are 0,1)
    * No polytime alogirthm known, or believed to exist
  * SAT: given a set of **boolean equations**, find a binary solution (variables are true, false)
    * No polytime alogirthm known, or believed to exist
* NP vs P
  * Definition
    * NP is the class of all search problems
    * P is the class of search problems solvable in poly-time
  * Search problem: given an instance of a problem, **find** a solution S
     * Requirement: must be able to efficiently **check** that S is a solution
  * Nondeteministic machine can **guess** the desired solution, 
    * NP is a class of search problems that are solvable in polynomial time on a **non-determinstic** Turing maching
* SAT: satisfiability
  * Q: how to solve an instance of SAT with n variables?
    * A: exhaustive search: try all 2^n truth assignment
  * Q: Can we do anything substantially more clever?
    * A: Conjecture: No polytime algorithm for SAT.
  * Q: Which search problems are in P?
    * A: No easy answers (we don't even know wether P = NP), but we can use reduction to identify some intractable ones
  * SAT reduces to ILP, TravelSalesMan, HamiltonPath etc
* NP-completeness
  * An NP problem is NP-complete if all problem in NP poly-time reduce to it
  * SAT is NP-complete
    * Implication: Polytime algorithm for SAT if and only if P = NP
* Exploiting intracatbility: crypotography
  * FACTOR: Given an m-bit integer x, find a nontrivial factor
  * Q: What is complexity of FACTOR?
    * A: In NP, but not known (or believed) to be in P or NP-complete
  * Q: What if P = NP?
    * A: Poly-time algorithm for factoring; modern e-conomy collapse
  * Cop
* Coping with intractability
  * Solve arbitrry instance of the problem: e.g.: 2-SAT
  * Solve the problem to optimality
  * Solve the problem in poly-time
* Hamilton Path: find a simple path that visits every vertex exactly once.
  * This is NP-complete
  * Longest path problem is also NP-complete

#### Template: Hamilton Path - NP Complete
```java
public class HamiltonPath {
    private boolean[] marked; //vertices on current path
    private int count = 0; //number of hamiltonian paths;

    public HamiltonPath(Graph G) {
        marked = new boolean[G.V()];
        for (int v = 0; v < G.V(); v++) {
            dfs(G, v, 1);
        }
    }

    private void dfs(Graph G, int v, int depth) {
        marked[v] = true;
        if (depth == G.V()) { //found one
            count++;
        }

        for (int w: G.adj(v)) {
            if (!marked[w]) {
                dfs(G, w, depth+1); //backtrak if w is already part of path
            }
        }

        marked[v] = false; //ONLY DIFFERENCE from regular dfs, and this is 2^N
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

Wiki on Backtracking: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

```java
backtrack(int[] input, List<List<String>> solutions, List<String> solution, int startIndex ) {

}
```

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


#### 425 Word Square 
```java
/*
Use Trie: Prefix -> List of Word
*/
class Solution {
    public List<List<String>> wordSquares(String[] words) {
        Map<String, Set<String>> prefix = new HashMap();
        for (String word: words) {
            for (int i = 1; i <= word.length(); i++) {
                String str = word.substring(0, i);
                if (!prefix.containsKey(str)) {
                    prefix.put(str, new HashSet());
                }
                prefix.get(str).add(word);
            }
        }
        
        List<List<String>> result = new ArrayList();
        List<String> candidate = null;
        
        for (String word: words) {
            candidate = new ArrayList();
            candidate.add(word);
            backtrack(candidate, result, 1, words[0].length(), prefix);
        }
        return result;
    }
    
    private void backtrack(List<String> candidate, List<List<String>> result, int wordCount, int squareSize, Map<String, Set<String>> prefix) {
        if (wordCount == squareSize) {
            result.add(new ArrayList(candidate));
            return;
        }
        
        StringBuilder sb = new StringBuilder();
        for (String cand: candidate) {
            sb.append(cand.charAt(wordCount));
        }
        
        if (!prefix.containsKey(sb.toString())) {
            return;
        }
        
        for (String next: prefix.get(sb.toString())) {
            candidate.add(next);
            backtrack(candidate, result, wordCount + 1, squareSize, prefix);
            candidate.remove(candidate.size() - 1);
        }
    }
}
```

#### More Questions
* [`MEDIUM`][LC93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)
* [`HARD`][LC425 Word Squares](https://leetcode.com/problems/word-squares/)
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


# Dynamic Programming Review


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

* [`MEDIUM`][Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)
```java
        int[] dp = new int[N]; //dp[i] is the maximum sum parition in K ways from 0..i
        
        for (int i = 0; i < N; i++) {
            int currentMax = 0;
            for (int k = 1; k <= K && i - k + 1 >= 0; k++) {
                curMax = Math.max(curMax, A[i-k+1]);
                dp[i] = Math.max(dp[i], (i >= k? dp[i - k] : 0) + curMax * k));
            }
        }
        return dp[N-1];
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

#####  * TODO Summarize Stacks
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
* [`MEDIUM`][LC649 Dota2 Senate](https://leetcode.com/problems/dota2-senate)
* [`HARD`][316 Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)


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