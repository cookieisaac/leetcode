# 每日手写 Cheatsheet
## Advanced
  * Binary Search
    * [LC34 Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
    * Find Peak Element II: 二分法深入理解
  * Quick Select:
    * [LC215 Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
  * BST
    * [LC173 Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
  * DFS: 
    * [LC78 Subsets](https://leetcode.com/problems/subsets)
    * [LC90 Subsets II](https://leetcode.com/problems/subsets-ii)
    * [LC46 Permutations](https://leetcode.com/problems/permutations)
    * [LC47 Permutations II](https://leetcode.com/problems/permutations-ii)
    * [LC140 Word Break II](https://leetcode.com/problems/word-break-ii/)
  * BFS:
    * [LC126 Word Ladder II](https://leetcode.com/problems/word-ladder-ii)
  * Union-Find: 
    * [LC305 Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)
  * Trie: 
    * [LC212 Word Search II](https://leetcode.com/problems/word-search-ii)
    * [LC425 Word Square II](https://leetcode.com/problems/word-squares/)
  * Sweep Line: 
    * [LC218 The Skyline Problem](https://leetcode.com/problems/the-skyline-problem) 扫描线经典入门题目
  * Deque: 
    * [LC239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)
* Monotonic Stack:
    * [LC84 Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)
  * Compiler:
    * [LC772 Calculator III](https://leetcode.com/problems/basic-calculator-iii/)

  * DP 
    * Rolling: House Robber: 滚动数组优化最简单的入门
    * Memorzation: Longest Increasing continuous Subsequence 2D: 记忆化搜索的经典题，此题只有记忆化搜索才能最优
    * DP Game: Coins in a Line III: 博弈问题和记忆化搜索的结合
    * DP Seqeunce: Edit Distance: 双序列常考题
    * DP Range: Stone-Game: 区间类DP的入门题, Burst Balloon
    * DP Backpack: Backpack II: 有价值的背包题目才有价值
  
## 递归模板 - 排列组合	 
  * [LC78 Subsets](https://leetcode.com/problems/subsets)
  * [LC90 Subsets II](https://leetcode.com/problems/subsets-ii)
  * [LC46 Permutations](https://leetcode.com/problems/permutations)
  * [LC47 Permutations II](https://leetcode.com/problems/permutations-ii)
  * NQueens - permutation type
  * Panlindrome Partitioning - subset type
  * Combination Sum - subset type
## 二分模板 - 有序数组的第一个和最后一个
  * [LC704 Binary Search](https://leetcode.com/problems/binary-search/)
  * [LC34 Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)
  * [LC35 Search Insertion Position](https://leetcode.com/problems/search-insert-position)
  * [LC4 Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)
## 二叉树遍历 - DFS迭代遍历+BFS遍历
  * [LC144 Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)
  * [LC94 Binary  Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) - 不需要Morris Traversal
  * [LC145 Binary  Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)
  * [LC102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)
## 分治算法 - MergeSort and QuickSort and divide&conquer
  * MergeSort - 分1合N
  * QuickSort - 分N合1
  * Template for DFS Divide&Conquer: Most of Binary Tree problem
    * [LC124 Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum) - 重要
    * [LC236 Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)
## 二叉搜索树 - validate, insert, delete and iterator
  * [LC98 Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)
  * [LC701 Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)
  * [LC450 Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst)
  * [LC173 Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator)
## Graph - Topological Sort
  * BFS Topological Sort Template
  * Search: Permutation DFS, Subsets DFS, BFS
## Stack
  * Monotonic Stack
  * [LC155 Min Stack](https://leetcode.com/problems/min-stack)
  * [LC84 Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)
## Heap
  * Template: Heapfiy and implementation
## Trie
  * Implementation
  * Word Search I && II



## Templates
* 什么时候Permutation模板?什么时候Subset模板？
* DFS: Find ALL solutions
  * O(N!) - permutation
  * O(2^N) - subset
* BFS: Find SHORTEST solution
  * O(N)
### DFS Search - Permutation - O(N!) - 所有叶节点才是结果
    * 遍历树的叶子节点才是result
    * 为什么`list.contains(nums)` 不优化为O(1)? 反正时间是O(N！),用了也不影响, 况且能这么跑的基本N<20
    * Permutation: 每一步都要考虑全部
```java
    public List<List<Integer>> permute(ArrayList<Integer> nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> state = new ArrayLsit<>();
        backtrack(result, list, nums);//Traverse entire search space
    }

    private backtrack(List<List<Integer>> result, List<Integer> list, ArrayList<Integer> nums) {
        if (list.size() == nums.size()) {
            result.add(new ArrayList<>(list)); //Important: Copy current state
            return;
        }
        for (Integer num: nums) {
            if (!result.contains(num)) {
                list.add(num);
                backtrack(result, list, nums);
                list.remove(list.size()-1); //Remove last one
            }
        }
    }
 ```

#### DFS Search - Subset - O(2^N) - 所有节点都是subset
    * 技巧:传递start,这样前面的不会再被考虑
    * 树中的每一个节点(不仅仅是叶节点)都是一个结果
    * Subset: 每一步都不需要考虑前面的元素
    * Subset II: 有重复, 先排序, 然后在同一层上每个数只考虑一次(第一个), 但剩余的元素会顺着向叶子传下去 `if (i != start && nums[i] == nums[i-1] {continue;}`
    * 如何考虑参数设计? 画Search Space图, 看要怎么去传递信息
```java
     public List<List<Integer>> subsets(ArrayList<Integer> nums) {
         List<List<Integer>> result = new ArrayList();
         Collections.sort(nums);
         backtrack(result, new ArrayList<Integer>(), nums, 0);
     }

     public backtrack(List<List<Integer>> result, List<Integer> list, ArrayList<Integer> nums, int start){
         result.add(new ArrayList<Integer>(list));

        for (int i = start; i < nums.length; i++) {
            list.add(num);
            backtrack(result, list, nums, start+1);
            list.remove(list.size()-1); //Remove last one
        }
     }
```


## Backtrack Template
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

## Template: Sliding Window

```java
for (i = 0; i < n; i++) {
    while (j < n) {
        if (满足条件) {
            j++;
            更新j状态
        } else (不满足条件){
            break;
        }
    }
    更新i状态
}
```

## Template: Union Find
```java
public class UnionFind {
    private int[] father = null;
    int find(int x) {
        if (father[x] == x) {
            return x;
        }
        //路径压缩
        return father[x] = find(father[x]);
    }

    //合并的root老大哥, 而不是小弟
    void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA != rootB) {
            father[rootA] = rootB;
        }
    }
}
```

## Template: BinarySearch按答案二分
```java
int start = 1, end = max;  //1. 找到可行解
while (start + 1 < end) { 
    int mid = start + (end - start)/2; //2.猜答案
    if (check(mid)) { //3. 检查答案
        start = mid; //4. 调整搜索范围
    } else {
        end = mid; //4. 调整搜索范围
    }
    //5.检查start, end
}
```

## QuickSelect: O(N)选出**第**K大
```java
public int partition(int[] nums, int l, int r) {
  //初始化左右指针和pivot
  int left = l, right = r;
  int pivot = nums[left];

  //进行partition
  while (left < right) {
    while (left < right && nums[right] >= pivot) {
      right--;
    }
    nums[left] = nums[right];
    while (left < right && nums[left] <= pivot) {
      left++;
    }
    nums[right] = nums[left];
  }

  //返回pivot到数组
  nums[left] = pivot;
  return left;
}
```


