Ordered by frequency as of March 21, 2018

## [763 Partition Labels](https://leetcode.com/problems/partition-labels)
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
```
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```
Note:
1. S will have length in range [1, 500].
2. S will consist of lowercase letters ('a' to 'z') only.

```java
//Greedy Algorithm
class Solution {
    private Map<Character, Integer> lookup = new HashMap<>();
    private String S;
    
    private int GetMax(int i) {
        return lookup.get(S.charAt(i));
    }
    
    public List<Integer> partitionLabels(String S) {
        List<Integer> solution = new LinkedList<>();
        
        for (int i = 0; i < S.length(); i++) {
            lookup.put(S.charAt(i), i);
        }
        
        int head = 0;
        for (int i = 0; i < S.length(); i++) {
            int last = GetMax(i);
            while (i < last ) {
                i++;
                if (GetMax(i) > last) last = GetMax(i);
            }
            solution.add(last - head + 1);
            head = i + 1;
        }
        return solution;
        
    }
}
```

## [1. Two Sum](https://leetcode.com/problems/two-sum)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement =  target - nums[i];
            
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
            
        }
        
        throw new IllegalArgumentException("No solution");
    }
}
```

## [3. Valid Parenthese](https://leetcode.com/problems/longest-substring-without-repeating-characters)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

```java
public class Solution {
    public boolean isValid(String s) {
        //Must use LinkedList instead of List to use addFirst, peakFirst and removeFirst
        LinkedList<Character> stack = new LinkedList<>(); 
        
        if (s.length() == 0) return true;
        
        Map<Character, Character> match = new HashMap<Character, Character>() {{
            put(')','(');
            put(']','[');
            put('}','{');
        }};
        
        for (int i = 0; i < s.length(); i++) {
            char symbol = s.charAt(i);
            if (symbol == '(' || symbol == '[' || symbol == '{') {
                stack.addFirst(symbol);
            } else if (symbol == ')' || symbol == ']' || symbol == '}') {
                if (stack.peekFirst() != match.get(symbol)) return false;
                else stack.removeFirst();
            } else {
                continue;
            }
        }
        
        return stack.isEmpty();
    }
}
```

## [200 Number of Islands](https://leetcode.com/problems/number-of-islands)

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
//Use DFS
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

## [675 Cut Off Trees for Golf Event](https://leetcode.com/problems/cut-off-trees-for-golf-event)

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
```
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
```
Example 2:
```
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
```
Example 3:
```
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
```
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
Hint: size of the given matrix will not exceed 50x50.

```java
class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        //Scan the forest, store and sort all height
        List<int[]> trees = new ArrayList<>();
        for (int row = 0; row < forest.size(); row++) {
            for (int col = 0; col < forest.get(0).size(); col++) {
                int height = forest.get(row).get(col);
                if (height > 1) {
                    trees.add(new int[]{height, row, col});
                }
            }   
        }
        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0])); //Sort by height
    
        //Go through trees ordered by height
        int answer = 0;
        int sourceRow = 0, sourceCol = 0; //Start from (0, 0)
        for (int[] tree: trees) {
            //Calculate th distance from previous height to current height
            int destinationRow = tree[1], destinationCol = tree[2];
            int distance = distance(forest, sourceRow, sourceCol, destinationRow, destinationCol);
            //If no path, then can't be reached
            if (distance < 0) return -1;
            //Otherwise update total distance, and current tree become the source
            answer += distance;
            sourceRow = tree[1];
            sourceCol = tree[2];
        }
    
        return answer;
    }
    
    //Use BFS
    public int distance(List<List<Integer>> forest, int sourceRow, int sourceCol, int destinationRow, int destinationCol) {
        Queue<int[]> queue = new LinkedList<>(); //{row, col, distance} tuple
        int R = forest.size(), C = forest.get(0).size();
        boolean [][] marked = new boolean[R][C];
        
        queue.add(new int[]{sourceRow, sourceCol, 0});
        marked[sourceRow][sourceCol] = true;
        
        //Up, Down, Left, Right ==> four neighbors in total for a node in matrix
        int[] neighborRowDiff = new int[]{-1, 1, 0, 0};
        int[] neighborColDiff = new int[]{0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            if (current[0] == destinationRow && current[1] == destinationCol) return current[2];
            //For all unmarked neighbor, mark it and put in queue
            for (int i = 0; i < 4; i++) { 
                int neighborRow = current[0] + neighborRowDiff[i];
                int neighborCol = current[1] + neighborColDiff[i];
                if (neighborRow >= 0 && neighborRow < R && neighborCol >= 0 && neighborCol < C //Valid neighbor index
                   && !marked[neighborRow][neighborCol] //Not visited
                   && forest.get(neighborRow).get(neighborCol) > 0) { //And is not a obscable
                    //mark and enqueue
                    marked[neighborRow][neighborCol] = true;
                    queue.add(new int[]{neighborRow, neighborCol, current[2]+1});
                }
                    
            }
        }
        return -1;     
    }
}
```

## [146 LRU Cache](https://leetcode.com/problems/lru-cache)

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

```java
public class LRUCache {
    //Double Linked List + Map to lookup Node in List
    Map<Integer, DNode> cache;
    DList list;
    final int capacity;
   
    private class DNode {
       int key;
       int value;
       DNode prev;
       DNode next;
       
       public DNode(int k, int v) {
           key = k;
           value = v;
           prev = null;
           next = null;
       }
    }
    
    private class DList {
        DNode head;
        DNode tail;
        
        public DList() {
            head = new DNode(0,0);
            tail = new DNode(0,0);
            head.next = tail;
            tail.prev = head;
        }
        
        public void addToHead(DNode node) {
            node.prev = head;
            node.next = head.next;
            head.next.prev = node;
            head.next = node;
        }
        
        //Note we return the Node here to later remove it from hashmap as well
        public DNode removeTail() {
            DNode last = tail.prev;
            last.prev.next = tail;
            tail.prev = last.prev;
            return last;
        }
        
        public void moveToHead(DNode node) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
            addToHead(node);
        }
    }
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        list = new DList();
        cache = new HashMap<>();
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        DNode valueNode = cache.get(key);
        list.moveToHead(valueNode);
        return valueNode.value;
    }
    
    public void put(int key, int value) {
        if (capacity == 0) return;
        if (cache.containsKey(key)) {
            DNode valueNode = cache.get(key);
            list.moveToHead(valueNode);
            valueNode.value = value;
        } else {
            if (cache.size() == capacity) {
                DNode removedNode = list.removeTail();
                cache.remove(removedNode.key);
            }
            DNode valueNode = new DNode(key, value);
            list.addToHead(valueNode);
            cache.put(key, valueNode);
        }
    }
}
```

## [48 Rotate Image](https://leetcode.com/problems/rotate-image)

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

```
Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

```java
public class Solution {
    public void rotate(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 1) {
            return;
        }
 
        int N = matrix.length;

        //Up down flip then symmetric swap => clockwise
        //Left right flip then symmetric swap => anti-clockwise
        for (int i = 0; i < N/2; i++) {
            for (int j = 0; j < N; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[N-i-1][j];
                matrix[N-i-1][j] = temp;
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
    }
}
```

## [297 Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree
```
    1
   / \
  2   3
     / \
    4   5
```
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            sb.append(serializeNode(node));
            if (node != null) {
                queue.offer(node.left);
                queue.offer(node.right);
            }
        }
        return sb.toString();
    }
    
    private String serializeNode(TreeNode node) {
        if (node == null) {
            return "null"+" ";
        } else {
            return Integer.toString(node.val) +" ";
        }
    }

    private TreeNode deserializeNode(String data) {
        if (data.equals("null") || data.equals("")) {
            return null;
        } else {
            return new TreeNode(Integer.parseInt(data));
        }
    }
    
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
        String[] parsed = data.split("\\s+");
        if (parsed.length == 0) return null;
        
        Queue<TreeNode> queue = new LinkedList<>();

        TreeNode root = deserializeNode(parsed[0]);
        queue.offer(root);
        for (int i = 1; i < parsed.length;) { //NOTE: no i++ here at for loop. Increment only happens after node is deserialized
            TreeNode parent = queue.poll();
            if (parent != null) {
                parent.left = deserializeNode(parsed[i]);
                i++;
                queue.offer(parent.left);
                if (i < parsed.length) {
                    parent.right = deserializeNode(parsed[i]);
                    i++;
                    queue.offer(parent.right);
                }
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

## [438 Find all anagrams in a string](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

Example 2:
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

Sliding Window
```
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

## [138 Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

```java
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;
        
        RandomListNode oldRunner = head;    //Runner for original list
        RandomListNode newRunner;           //Runner for new list
        
        //Pass One: Build all nodes in new list with value, use next pointer to interleave
        while (oldRunner != null) {
            newRunner = new RandomListNode(oldRunner.label);
            //Store oldRunner next
            newRunner.next = oldRunner.next;
            //Store current newRunner
            oldRunner.next = newRunner;
            //Advance oldRunner to its original next
            oldRunner = newRunner.next;
        }
        
        //Pass Two: Construct Random Pointer for new List
        RandomListNode newHead = head.next;
        newRunner = newHead;
        oldRunner = head;
        while (oldRunner != null) {
            //Construct newRunner random
            newRunner.random = oldRunner.random == null? null : oldRunner.random.next;
            //Advance oldRunner and newRunner
            oldRunner = newRunner.next;
            newRunner = oldRunner == null ? null : oldRunner.next;
        }
        
        //Rass Three: Restore next pointer for all lists
        newRunner = newHead;
        oldRunner = head;
        while (oldRunner != null) {
            //Restore newRunner/oldRunner next pointer
            oldRunner.next = newRunner.next;
            newRunner.next = oldRunner.next == null? null: oldRunner.next.next;
            //Advance newRunner and oldRunner
            oldRunner = oldRunner.next;
            newRunner = newRunner.next;   
        }
        return newHead;
    }
}
```

## [236 Lowest Common Ancestorof a Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        return left == null ? right : (right == null? left : root );
        /* //Same as following
        if (left == null) return right;
        else if (right == null) return left;
        else return root;
        */
    }
}
```

## [5 Longest Panlindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
```
Input: "babad"

Output: "bab"
```
Note: "aba" is also a valid answer.
 

Example:
```
Input: "cbbd"

Output: "bb"
```

```
class Solution {
    //Algorithm: O(N^2), Space: O(1)
    public String longestPalindrome(String s) {
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            //If the panlindrome is of odd characters
            int length1 = expandAroundCenter(s, i, i);
            //If the panlindrome is of even characters
            int length2 = expandAroundCenter(s, i, i+1);
            int length = Math.max(length1, length2);
            if (length > end - start) {
                start = i - (length - 1) / 2;
                end = i + length / 2;
            }
        }
        return s.substring(start, end+1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

## [121 Best Time to Buy and Sell Stocks](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

```java
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 1) return 0;
        
        //Compute Day to Day price changes
        int[] diff = new int[prices.length - 1];
        for (int i = 0; i < prices.length - 1; i++) {
            diff[i] = prices[i+1] - prices[i];
        }
        
        //Find the largest sum of continuous diff
        int max = 0; //Max Profit
        int profit = 0; //Current Profit
        for (int i = 0; i < diff.length; i++) {
            profit += diff[i];
            if (profit < 0) profit = 0;
            if (profit > max) max = profit;
        } 
        return max;
    }
}
```

## [238 Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums.length < 2) return nums;
        
        int[] result = new int[nums.length];
        result[0] = 1;
        //First Pass: multiply everything to the left
        for (int i = 1; i < nums.length; i++) {
            result[i] = result[i-1]*nums[i-1];
        }
        
        //Second Pass: multiply everything to the right;
        int right = 1;
        for (int j = nums.length - 1; j >= 0; j--) {
            result[j] = result[j] * right;
            right = nums[j] * right;
        }
        return result;
    }
}
```

## [711 Number of Distinct Island II](https://leetcode.com/problems/number-of-distinct-islands-ii/description/)


Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1. 

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.

```java
class Solution {
    //Get adjacent neighbor of a given coordinate
    int[][] neighbors={{-1,0}, {1,0}, {0,-1}, {0,1}};
    //Generate 8 different transformations of a given coordinate
    //(X,Y), (X,-Y), (-X,Y), (-X,-Y)
    //(Y,X), (Y,-X), (-Y,X), (-Y,-X)
    int[][] transforms = {{1,1}, {1, -1}, {-1, 1}, {-1, -1}};
    
    public int numDistinctIslands2(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int M = grid.length, N = grid[0].length;
        Set<String> islands = new HashSet<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) {
                    List<int[]> island = new ArrayList<>(); //A list of all coordinates
                    dfs(grid, i, j, island);
                    //printIsland(island);
                    String islandKey = normalize(island);
                    islands.add(islandKey);
                }
            }
        }
        return islands.size();
    }
            
    private void dfs(int[][] grid, int i, int j, List<int[]> island) {
        island.add(new int[]{i, j});
        grid[i][j] = -1; //Mark as visited
        
        for (int[] neighbor: neighbors) {
            int x = i + neighbor[0];
            int y = j + neighbor[1];
            if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && grid[x][y] == 1) {
                dfs(grid, x, y, island);
            }
        }
    }
    
    private void printIsland(List<int[]> island) {
        System.out.println("===Island===");
        for (int[] coordinate: island) {
            System.out.println(coordinate[0]+","+coordinate[1]);
        }
    }
    
    private String normalize(List<int[]> island) {
        List<String> forms = new ArrayList<>();
        //Generate 8 different transformations
        //List1: (x, y), (x, -y), (-x, y), (-x, -y)
        //List2: (y, x), (-y, x), (y, -x), (-y, -x)
        for (int[] transform: transforms) {
            List<int[]> list1 = new ArrayList<>();
            List<int[]> list2 = new ArrayList<>();
            for (int[] coordinate: island) {
                list1.add(new int[]{coordinate[0]*transform[0], coordinate[1]*transform[1]});
                list2.add(new int[]{coordinate[1]*transform[1], coordinate[0]*transform[0]});
            }
            forms.add(getKey(list1));
            forms.add(getKey(list2));
        }
        
        //Sort the keys: take the first one as the representative key
        Collections.sort(forms);
        return forms.get(0);
    }
            
    private String getKey(List<int[]> island) {
        //sort the cells before generate the key
        Collections.sort(island, (a, b) -> {
            return a[0]!=b[0] ? a[0]-b[0] : a[1]-b[1];
        });
        
        StringBuilder sb = new StringBuilder();
        //Get the first coordinate of sorted island coordinates
        int x=island.get(0)[0], y = island.get(0)[1];
        for (int[] coordinate: island) {
            sb.append((coordinate[0]-x)+":"+(coordinate[1]-y)+":");
        }
        return sb.toString();
    }
}
```

## [239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 ```
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

```java
public class Solution {
    public void inspect(int i, Deque<Integer> queue, String str, int[] nums) {
        System.out.print("nums[" + i + "]="+nums[i]+", " + str+ ", [");
        for (int num: queue) {
            System.out.print(nums[num]+" ");
        }
        System.out.print("], indexes are: [");
        for (int num: queue) {
            System.out.print(num+" ");
        }
        System.out.println("]");
    }
    
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) {
            return new int[0];
        }
		
        int[] results = new int[nums.length - k + 1];
		//iterator index for results
        int ri = 0;
		
        //Deque is double ended queue
        //API looks like follow: peek/poll <= [a0, a1, a2, ... aNew] <= offer/peekLast/pollLast
        //Use a deque to store the index of potential largest number in window
        //INVARIANT: The underlying value indexed by deque should be decreasing
        //[5, -3, -1], and if 4 comes along, then if should be [5, 4]
		Deque<Integer> q = new ArrayDeque<>();
        
		for (int i = 0; i < nums.length; i++) {
            //System.out.println("===========Current i: "+i+"============");
		    //Step1: Clear out of range index from front
            //current index to last index is greater than window: a.k.a: i - q.peek() + 1 > k
		    while (!q.isEmpty() && i - q.peek() + 1 > k ) { 
                //remove older indexes since they are out of range k from current index i
		        q.poll();
		        //inspect(i, q, "index out of range, POLL", nums);
		    }
		    
            //Step2: Clear out useless value from back, maintain decreasing invariant
            //Between the oldest index to current index i, 
            //if recent number is smaller than current number
		    //remove this smaller numbers as they are useless
            //since the largest would be at least larger than current num
		    while(!q.isEmpty() && nums[q.peekLast()] < nums[i]) {
		        q.pollLast();
		        //inspect(i, q, "last less than current, POLL_LAST", nums);
		    }
		    
            //Step3: Add to deque
		    //q contains index of the potential maximum value, not the value itself
		    q.offer(i);
		    //inspect(i, q, "add new i,OFFER", nums);
		    
            //Step4: Form result based on deque front
            //A valid window size has been formed
            if (i >= k - 1) {
		        //inspect(i, q, "window size reached, update results PEEK", nums);
		        results[ri] = nums[q.peek()];
		        ri++;
		    }
		}
		return results;
    }
}
```

## [42 Trapping Rain Water]()
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

![alt text](https://leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 

```java
public class Solution {
    public void inspect(int i, int j, int[] height, int plank, int result) {
        System.out.println("i=" + i +", j=" + j +", height[i]=" + height[i] +",height[j]=" + height[j] + ", plank=" + plank +", result="+result);
    }
    
    //If both height of left and right boundary are greater than current plank, then plank is the smaller of the boundary
    //The boundary with smaller height contributes to the result will move closer to the center
    public int trap(int[] height) {
        int i = 0, j = height.length - 1, result = 0, plank = 0;
        while (i <= j) {
            //inspect(i,j, height, plank, result);
            plank = Math.min(height[i], height[j]) > plank ? Math.min(height[i], height[j]): plank;
            result = height[i] >= height[j]? result + (plank - height[j--]):result + (plank - height[i++]);
        }
        return result;
    }
}
```

## [23 Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Time complexity of my implementation is `O(N log k)`

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    
    //Keep the head from each list in a priority queue
    //Select the smallest node of the heap
    //Put the next node of this smallest node back to the heap
    //Iterate till heap is empty
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        if (lists.length == 1) return lists[0];
        
        //Keep the head from each list in a priority queue
        PriorityQueue<ListNode> heap = new PriorityQueue<>((x, y) -> Integer.compare(x.val, y.val));
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                heap.offer(lists[i]);
            }
        }
        
        ListNode pseudoHead = new ListNode(-1); //A pseudo head
        ListNode runner = pseudoHead;
        while (!heap.isEmpty()) {
            //Select the smallest node of the heap
            ListNode next = heap.poll();
            
            //Put the next node of this smallest node back to the heap
            if (next != null && next.next != null) {
                heap.offer(next.next);
            }
            
            //Construct merged list
            runner.next = next;
            
            //Advance runner
            runner = next;
        }
        return pseudoHead.next;
    }
}
```

## [460 LFU Cache](https://leetcode.com/problems/lfu-cache/description/)

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
```
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

```java
//Use LinkedHashSet to store keys as it preserves the order of insertion. 
//The time complexity of basic methods is O(1).
public class LFUCache {
    private HashMap<Integer, Integer> vals; //key -> value
    private HashMap<Integer, Integer> keyToFreq; //key -> freq
    private HashMap<Integer, LinkedHashSet<Integer>> freqToKeys; // freq -> list of keys
    
    private final int capacity;
    private int min = 1; //Current min frequency count
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        vals = new HashMap<>();
        keyToFreq = new HashMap<>();
        freqToKeys = new HashMap<>();
        freqToKeys.put(1, new LinkedHashSet<>());
    }
    
    public int get(int key) {
        //Cache miss: return -1
        if(!vals.containsKey(key))
            return -1;
        
        //Cache hit: add frequency by 1
        //Update keyToFreq, freqToKeys, and potentially global min freq
        int freq = keyToFreq.get(key);
        keyToFreq.put(key, freq+1);
        freqToKeys.get(freq).remove(key);
        if(freq == min && freqToKeys.get(freq).size()==0)
            min++;
        if(!freqToKeys.containsKey(freq+1))
            freqToKeys.put(freq+1, new LinkedHashSet<>());
        freqToKeys.get(freq+1).add(key);
        return vals.get(key);
    }
    
    public void put(int key, int value) {
        if(capacity <= 0) return;
        
        //Cache hit: update value and do a get to trigger internal update
        if(vals.containsKey(key)) {
            vals.put(key, value);
            get(key);
            return;
        } 
        
        //Cache miss: evict a least frequently used item, then add new entry
        if(vals.size() >= capacity) {
            int evict = freqToKeys.get(min).iterator().next();
            freqToKeys.get(min).remove(evict);
            vals.remove(evict);
        }
        //Since this is a cache miss, current element only been used once, hence the lowest frequency is 1 now
        min = 1; 
        vals.put(key, value);
        keyToFreq.put(key, 1);
        freqToKeys.get(1).add(key);
    }
}
/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

## [17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![alt text](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

```java
public class Solution {
    private final Map<Character, String> translate = new HashMap<Character, String>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};
    
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return new LinkedList<String>();
        
        List<String> solutions = new ArrayList<>();
        backtrack(solutions, "", digits);
        return solutions;
    }
    
    private void backtrack(List<String> solutions, String prefix, String digits) {
        if (prefix.length() == digits.length()) { //Emit Solution
            solutions.add(prefix);
        } else { //Otherwise, iterate all ways to make next steps
            for (char c: translate.get(digits.charAt(prefix.length())).toCharArray()) {
                prefix += c; //Take a step: append one letter
                backtrack(solutions, prefix, digits); //Backtrack
                prefix = prefix.substring(0, prefix.length()-1); //Reverse the step: remove that letter
            }
        }       
    }
}
```

## [387 First Unique Character in the String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
Note: You may assume the string contain only lowercase letters.

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] map = new int[128];
        for (char c: s.toCharArray()) map[c]++;
        for (int i = 0; i < s.length(); i++)
            if (map[s.charAt(i)] == 1) return i;
        return -1;
    }
}
```

## [127 Word Ladder](https://leetcode.com/problems/word-ladder/description/)

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
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

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
	
        return path.pathLength(sg.getIndex(endWord));
    }
}

```

## [682 Baseball Game](https://leetcode.com/problems/baseball-game/description/)
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.

```java
class Solution {
    public int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack<>();  //Stack to hold each rounds score
        for (String op: ops) {
            if (op.equals("C")) {
                stack.pop();
            } else if (op.equals("D")) {
                int last = stack.peek();
                stack.push(2 * last);
            } else if (op.equals("+")) {
                int last = stack.pop();
                int secondLast = stack.peek();
                stack.push(last);
                stack.push(last + secondLast);
            } else {
                stack.push(Integer.parseInt(op));
            }
        }
        
        int sum = 0;
        while (!stack.isEmpty()) {
            sum += stack.pop();
        }
        return sum;
    }
}
```

## [2 Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode runner = head;
        int carry = 0;
        
        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;
            runner.next = new ListNode(sum % 10);
            carry = sum / 10;
            l1 = l1.next; l2 = l2.next; runner = runner.next;
        }
        
        while (l1 != null) {
            int sum = l1.val + carry;
            runner.next = new ListNode(sum % 10);
            carry = sum / 10;
            l1 = l1.next; runner = runner.next;
        }
        
        while (l2 != null) {
            int sum = l2.val + carry;
            runner.next = new ListNode(sum % 10);
            carry = sum / 10;
            l2 = l2.next; runner = runner.next;
        }
        
        if (carry != 0) runner.next = new ListNode(carry);
        
        return head.next;
    }
}
```

## [206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

Reverse a singly linked list.

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode prev = null;
        ListNode runner = head;
        ListNode next = runner.next;
        
        while (runner != null) {
            next = runner.next;
            runner.next = prev;
            prev = runner;
            runner = next;
        }
        
        return prev; 
    }
}
```

## [155 Min Stack](https://leetcode.com/problems/min-stack/description/)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

```java
class MinStack {
    private ArrayList<Integer> valStack;
    private ArrayList<Integer> minStack;
    
    public MinStack() {
        valStack = new ArrayList<>();
        minStack = new ArrayList<>();
    }
    
    public void push(int x) {
        valStack.add(x);
        minStack.add(
            minStack.isEmpty() ? x : Math.min(minStack.get(minStack.size()-1), x));
    }
    
    public void pop() {
        if (valStack.size() < 1) return;
        valStack.remove(valStack.size()-1);
        minStack.remove(minStack.size()-1);
    }
    
    public int top() {
        return valStack.get(valStack.size()-1);
    }
    
    public int getMin() {
        return minStack.get(minStack.size()-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

## [235 Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
```
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
```
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        return left == null? right : (right == null? left : root);
    }
}
```
## [240 Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
Given target = 5, return true.

Given target = 20, return false.

```java
class Solution {
    //Search from top right, and search along reverse diagonal line
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) return false;
        
        int row = 0, col = matrix[0].length - 1;
        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) return true;
            else if (matrix[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
}
```
## [449 Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private String serializeNode(TreeNode node) {
        if (node == null) return "null"+" ";
        else return Integer.toString(node.val) + " ";    
    }
    
    private TreeNode deserializeNode(String data) {
        if (data.equals("") || data.equals("null")) return null;
        else return new TreeNode(Integer.parseInt(data));
    }
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode parent = queue.poll();
            if (parent != null) {
                queue.offer(parent.left);
                queue.offer(parent.right);
            }
            sb.append(serializeNode(parent));
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] parsed = data.split("\\s+");
        if (parsed.length == 0) return null;
        
        Queue<TreeNode> queue = new LinkedList<>();
        
        TreeNode root = deserializeNode(parsed[0]);
        queue.offer(root);
        for (int i = 1; i < parsed.length; ) {
            TreeNode parent = queue.poll();
            if (parent != null ) {
                parent.left = deserializeNode(parsed[i]);
                i++;
                queue.offer(parent.left);
                if (i < parsed.length) {
                    parent.right = deserializeNode(parsed[i]);
                    i++;
                    queue.offer(parent.right);
                }
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

## [49 Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:
```
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
Note: All inputs will be in lower-case.

```java
class Solution {
    private String getKey(String str) {
        char[] temp = str.toCharArray();
        Arrays.sort(temp);
        return Arrays.toString(temp);
    }
    
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str: strs) {
            String key = getKey(str);
            if (!map.containsKey(key)) map.put(key, new ArrayList<String>());
            map.get(key).add(str);
        }
        return new ArrayList<>(map.values());
    }
}
```

## [234 Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    
    //Use fast runner/slow runner to find the middle point
    //Flip the direction from the middle point to the end
    //Use two pointer to run from head and tail at the same time towards the center
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        
        //Step 1: Find the middle point
        ListNode walker = head, runner = head;
        while(runner != null && runner.next != null) {
            walker = walker.next;
            runner = runner.next.next;
        }
        
        //Step 2: Flip the second half of the list 
        ListNode reverseHead;
        if (runner == null) 
            reverseHead = reverse(walker); //[0 -> 1 -> 2 -> 3 -> 4 -> 5], walker will be at 3, the beginning of second half
        else  //runner != null && runner.next == null
            reverseHead = reverse(walker.next); //[0 -> 1 -> 2 -> 3 -> 4], walker will be at 2, the exact middle point
        
        //Step 3: compare by palindrome definition
        ListNode runnerFront = head;
        ListNode runnerBack = reverseHead; 
        while (runnerBack != null && runnerFront != null) {
            if (runnerBack.val != runnerFront.val) return false;
            runnerBack = runnerBack.next;
            runnerFront = runnerFront.next;
        }
        return true;
    }
    
    private ListNode reverse(ListNode head) {
        ListNode node = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = node;
            node = head;
            head = next;
        }
        return node;
    }
}
```

## [380 Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:
```
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
```

```java
class RandomizedSet {
    ArrayList<Integer> values; //Serve as an array of values
    HashMap<Integer, Integer> indexes; //value -> (index in array list)
    Random random = new Random();
    
    /** Initialize your data structure here. */
    public RandomizedSet() {
        values = new ArrayList<>();
        indexes = new HashMap<>();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (indexes.containsKey(val)) return false;
        indexes.put(val, values.size());
        values.add(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!indexes.containsKey(val)) return false;
        //NOTE: cannot use `values.remove(indexes.get(val))` as this will be O(N)
        //IDEA: swap the one to be deleted to the last, then remove last
        int last = values.get(values.size()-1);
        int toDeleteIndex = indexes.get(val);
        //1. Overwrite toDelete with Last
        values.set(toDeleteIndex, last);
        indexes.put(last, toDeleteIndex);
        //2. Remove last
        values.remove(values.size() - 1); //This operation is O(1);
        indexes.remove(val);
        
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return values.get(random.nextInt(values.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

## [98 Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
```
    2
   / \
  1   3
```
Binary tree [2,1,3], return true.

Example 2:
```
    1
   / \
  2   3
```
Binary tree [1,2,3], return false.


```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {   
    //NOTE: Root value must be greater/less than ALL the value of its descendants, not just its children.
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean isValidBST(TreeNode root, long minVal, long maxVal) {
        if (root == null) return true;
        if (root.val >= maxVal || root.val <= minVal) return false;
        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
    }
}
```

## [545 Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/description/)

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1
```
Input:
  1
   \
    2
   / \
  3   4
```
Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2
Input:
```
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
```
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 

// IDEA: 1 Pass PreOrder PostOrder Hybrid
// As a node, my left child will inherit my leftness, but might lose my rightness if I have a right child.
// As a node, my right child will inherit my rightness, but might lose my leftness if I have a left child.

// If I am a left bound, I should appear before my 2 children - preorder
// If I am a right bound, I should appear after my 2 children - postorder
// If I am neither left nor right AND I am a leave, then I must be bottom.
class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root != null) {
            result.add(root.val);
            getBounds(root.left, true, false, result);
            getBounds(root.right, false, true, result);
        }
        return result;
    }
    
    //Three combination for <isLeftBound, isRightBound>: 
    //  - (true, false): left boundary
    //  - (false, true): right boundary
    //  - (false, false): if leaves, then bottom boundary
    // NOTE: there will never be the case where the combinaiton is (true, true)
    private void getBounds(TreeNode node, boolean isLeftBound, boolean isRightBound, List<Integer> result) {
        if (node == null) return;
        
        //Step 1: Add Left Bound
        if (isLeftBound) result.add(node.val);
        
        //Step 2: Add Bottom: a.k.a Leaves that are not on the Left/Right Boundary
        if (!isLeftBound && !isRightBound && node.left == null && node.right == null) result.add(node.val);
        
        //Step 3: Recursive on Left and Right Child to complete all of their left, bottom and right
        //Recursion on Left Child: my left child will not be a right boundary anymore if I have a right child
        getBounds(node.left, isLeftBound, isRightBound && node.right == null, result);
        //Recursion on Right: my right child will not be a left bondary anymore if I have a left child
        getBounds(node.right, isLeftBound && node.left == null, isRightBound, result);
        
        //Step 4: Add Right Bound
        if (isRightBound) result.add(node.val);
    }
}
```

## [21 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {  
        ListNode dummyHead = new ListNode(0);
        ListNode runner = dummyHead;
        
        //Merge L1 and L2
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val ) {
                runner.next = new ListNode(l1.val);
                l1 = l1.next;
                runner = runner.next;
            } else {
                runner.next = new ListNode(l2.val);
                l2 = l2.next;
                runner = runner.next;
            }
        }
        
        //Finish L1 leftover
        while (l1 != null) {
            runner.next = new ListNode(l1.val);
            l1 = l1.next;
            runner = runner.next;
        }
        
        //Finish L2 leftover
        while (l2 != null) {
            runner.next = new ListNode(l2.val);
            l2 = l2.next;
            runner = runner.next;
        }
        
        return dummyHead.next;
    }
}
```

## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int head = 0, length = 0;   //Maximum String so far
        int begin = 0, end = 0;     //Window
        int[] map = new int[128];   //Feature Map
        int diff = 0;               //Feature
        
        while (end  < s.length()) {
            //Move end till the window is invalid 
            //(Before increase, if map[c] == 1 means c is in the window now)
            if (map[s.charAt(end++)]++ == 1) diff++;
            //Move begin to make window valid 
            //(After decrease, it should be map[c] == 1, which means c is in the window only once now)
            while (diff > 0) {
                if (map[s.charAt(begin++)]-- == 2) diff--;
            }
            //Record this window if it's larger
            if (end - begin > length) length = end - (head = begin);
        }
        return length;
    }
}
```

## [139. Word Break](https://leetcode.com/problems/word-break/description/)

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] breakable = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (String word: wordDict) {
                if (s.substring(i).startsWith(word) && (i == 0 || breakable[i-1] == true)) {
                    breakable[i+word.length()-1] = true;
                }
            }
        }
        return breakable[s.length()-1];
    }
}
```

## [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //Let Runner1 traverse A+B, whereas Runner2 traverse B+A, then they will at least at last null
        //A would traverse a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3
        //B woudl traverse b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3
        if (headA == null || headB == null) return null;
        ListNode runner1 = headA, runner2 =  headB;
        while (runner1 != runner2 ) {
            runner1 = runner1==null? headB : runner1.next; //traverse B after A
            runner2 = runner2==null? headA : runner2.next; //traverse A after B
        }
        return runner1;
    }
}
```

## [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/description/)
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
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

```java
public class Solution {
    //A copy of dictionary, INPUT
    private Set<String> dict;
    
    //Adjacency Map of SymbolGraph, INPUT by dict, OUTPUT to bfs, dfs
    private HashMap<String, ArrayList<String>> nodeNeighbors = new HashMap<>();
    
    //Path Length from begin word to ALL word in dict, INPUT by bfs, output to dfs
    private HashMap<String, Integer> distance;
    
    public List<List<String>> findLadders(String start, String end, List<String> wordList) {
        //Step 1: Init all necessary auxiliary information
        this.dict = new HashSet<String>(wordList);
        dict.add(start);  
        
        this.nodeNeighbors = new HashMap<>();
        for (String word : dict) this.nodeNeighbors.put(word, new ArrayList<String>());
        
        this.distance = new HashMap<>();
        
        //Step 2: BFS to Build node adjacency list AND distance lookup        
        bfs(start, end);  
        
        //Step 3: Backtrack on all possible path
        List<List<String>> result = new ArrayList<List<String>>();
        ArrayList<String> pathPrefix = new ArrayList<String>();
        dfs(start, end, pathPrefix, result);
        
        return result;
    }
    
    // BFS: Trace every node's distance from the start node (level by level).
    private void bfs(String start, String end) {
        Queue<String> queue = new LinkedList<String>();
        queue.offer(start);
        distance.put(start, 0); //Serve as the marked[] to see if nodes are already visited

        
        while (!queue.isEmpty()) {
            int level = queue.size(); //NOTE: Used to explore node level by level
            boolean foundEnd = false;
            
            //NOTE: MUST explore all nodes of the level where end word is in.
            for (int i = 0; i < level; i++) { 
                //Get a word
                String currentWord = queue.poll();

                //Update relevant information: distance & neighbor
                int currentDistance = distance.get(currentWord);
                nodeNeighbors.put(currentWord, getNeighbors(currentWord));

                //Enqueue unvisited neighbor
                for (String neighbor: nodeNeighbors.get(currentWord)) {
                    //nodeNeighbors.get(currentWord).add(neighbor);
                    if (!distance.containsKey(neighbor)) { 
                        distance.put(neighbor, currentDistance + 1);
                        queue.offer(neighbor);
                        //DON'T BREAK HERE RIGHT AWAY. WAIT TILL YOU FINISH ALL NODES AT THIS LEVEL
                        if (neighbor.equals(end)) foundEnd = true; 
                    }
                }
            }
            
            if (foundEnd) break;
        }
    }
    
    // Find all next level nodes.    
    private ArrayList<String> getNeighbors(String node) {
        ArrayList<String> result = new ArrayList<String>();
        char chs[] = node.toCharArray();

        //Compute all different variations of the word, and see if it's in the dictionary
        for (char ch ='a'; ch <= 'z'; ch++) {
            for (int i = 0; i < chs.length; i++) {
                if (chs[i] == ch) continue;
            
                char old_ch = chs[i];
                chs[i] = ch;
                if (dict.contains(String.valueOf(chs))) {
                    result.add(String.valueOf(chs));
                }
                chs[i] = old_ch;
            }
        }
        return result;
    }
    
    // DFS: output all paths with the shortest distance using backtracking
    private void dfs(String currentWord, String endWord, ArrayList<String> pathPrefix, List<List<String>> result) {
        //Step 1: Take a step with currentWord
        pathPrefix.add(currentWord);

        //Step 2: Explore on all possible next steps
        if (endWord.equals(currentWord)) {
            //Step 2.1: If already reached end, no need to explore next stap
            result.add(new ArrayList<String>(pathPrefix));
        } else {
            //Step 2.2: Otherwise, the next step should be the neighbor AND one step larger from current node to end
            for (String nextWord : nodeNeighbors.get(currentWord)) {            
                if (distance.get(nextWord) == distance.get(currentWord) + 1) {
                    dfs(nextWord, endWord, pathPrefix, result);
                }
            }
        }

        //Step 3: Take the step back
        pathPrefix.remove(pathPrefix.size() - 1);
    }
}
```

