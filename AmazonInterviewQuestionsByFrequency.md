Ordered by frequency as of March 21, 2018

## Random Fun Fact

Group Theory Stuff

* Dihedral Group of Order 8: 711 Number of Island https://www.youtube.com/watch?v=mvmuCPvRoWQ starting at 2:27 ish
* Matrix Flip: 48 Rotate Matrix https://www.youtube.com/watch?v=mvmuCPvRoWQ starting at 4:16 ish

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
## [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


```java
//O(N*lgN)
class Solution {
    public int findKthLargest(int[] nums, int k) {
        //A MIN heap of all the large numbers in nums
        PriorityQueue<Integer> heap = new PriorityQueue<>(k);
        heap.offer(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (heap.size() < k || nums[i] > heap.peek()) {
                if (heap.size() == k) heap.poll();
                heap.offer(nums[i]);
            }
        }
        
        return heap.peek();
    }
}
```

```java
public class Solution {
    public int findKthLargest(int[] nums, int k) {
        return quickselect(nums, nums.length-k);
    }
    
    public static void quicksort(int[]nums) {
        sort(nums, 0, nums.length-1);
    }
    
    public static void sort(int[]nums, int lo, int hi) {
        if (lo >= hi) return; //no action if only one element
        int j = partition(nums, lo, hi);
        sort(nums, lo, j-1);
        sort(nums, j+1, hi); 
    }
    
    public static int quickselect(int[]nums, int k) {
        int lo = 0, hi = nums.length-1;
        while (hi > lo) {
            int j = partition(nums, lo, hi);
            if (j < k) lo = j + 1;
            else if (j > k) hi = j - 1;
            else break;
        }
        return nums[k];
    }
    
    public static void shuffle(int[]nums) {
        Random rand = new Random();
        for (int i = 1; i < nums.length; i++) {
            int r = rand.nextInt(i+1);
            exch(nums, i, r);
        }
    }
    
    public static int partition(int[]nums, int lo, int hi) {
        int i=lo, j=hi+1;
        int v=nums[lo];
        while (true) {
            while(nums[++i] < v) if (i == hi) break;
            while(nums[--j] > v) if (j == lo) break;
            if (i >= j) break;
            exch(nums, i, j);
        }
        exch(nums, lo, j);
        return j;
    }
    
    public static void exch(int[] nums, int i, int j) {
        int swap = nums[i];
        nums[i] = nums[j];
        nums[j] = swap;
    }
    
    public void inspect(int[] nums) {
        System.out.print("nums: [ ");
        for (int num: nums) {
            System.out.print(num+" ");
        }
        System.out.println("]");
    }
}
```

## [517. Super Washing Machines](https://leetcode.com/problems/super-washing-machines/description/)

You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time .

Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

Example1
```
Input: [1,0,5]

Output: 3

Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   
```

Example2
```
Input: [0,3,0]

Output: 2

Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
```

Example3
```
Input: [0,2,0]

Output: -1

Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 
```

Note:
The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].

```java
public class Solution {
    /*
    Let me use an example to briefly explain this. For example, your machines[] is [0,0,11,5]. 
    So your total is 16 and the target value for each machine is 4. 
    Convert the machines array to a kind of gain/lose array, we get: [-4,-4,7,1]. 
    Now what we want to do is go from the first one and try to make all of them 0.
    
    To make the 1st machines 0, you need to give all its “load” to the 2nd machines.
    So we get: [0,-8,7,1]
    then: [0,0,-1,1]
    lastly: [0,0,0,0], done.
    
    You don’t have to worry about the details about how these machines give load to each other. 
    In this process, the least steps we need to eventually finish this process is determined by 
        - the peak of abs(cnt) and 
        - the max of “gain/lose” array. 
    In this case, the peak of abs(cnt) is 8 and the max of gain/lose array is 7. So the result is 8.

    Some other example:
    machines: [0,3,0]; gain/lose array: [-1,2,-1]; max = 2, cnt = 0, -1, 1, 0, its abs peak is 1. So result is 2.
    machines: [1,0,5]; gain/lose array: [-1,-2,3]; max = 3, cnt = 0, -1, -3, 0, its abs peak is 3. So result is 3.
    */
    public int findMinMoves(int[] machines) {
        //If the total clothes cannot be equally divided, then no solution
        int total = 0; 
        for(int i: machines) total += i;
        if( total % machines.length != 0) return -1;

        int avg = total/machines.length;
        int cnt = 0; //Net Gain/Lose so far, ie: sum of gain/lose from the machines ahead of me
        int max = 0; //Maximum of Peak of abs(cnt) and Value of "gain/lose" array so far
        for(int load: machines){
            cnt += load-avg; //load-avg is "gain/lose"
            max = maxOf3(max, Math.abs(cnt), load-avg);
        }
        return max;
    }
    
    private int maxOf3(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }
}
```

## [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();
        
        Arrays.sort(sc);
        Arrays.sort(tc);
        
        return Arrays.toString(sc).equals(Arrays.toString(tc));
    }
}
```

## [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int count = queue.size(); //All the nodes at this level
            List<Integer> layer = new LinkedList<>();
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                if (node != null) {
                    layer.add(node.val);
                    queue.offer(node.left);
                    queue.offer(node.right);
                }
            }
            if (layer.size() > 0) result.add(layer);
        }
        
        return result;
    }
}
```

##  [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode walker = head;
        ListNode runner = head;
        
        while (runner != null && runner.next != null) {
            walker = walker.next;
            runner = runner.next.next;
            if (walker == runner) return true;
        }
        return false;
    }
}
```

## [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.
```
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[]{0,0};
        for (int i = 0, j = nums.length - 1; i < j; ) {
            if (nums[i] + nums[j] == target) return new int[]{i+1, j+1};
            else if (nums[i] + nums[j] > target) j--;
            else i++;
        } 
        return result;
    }
}
```

## [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/description/)

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

Example 2:
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

```java
class Solution {
    ArrayList<TreeSet<String>> freqToWords = new ArrayList<>();
    HashMap<String, Integer> wordToFreq = new HashMap<>();
    int maxFreq = 0;
    
    public List<String> topKFrequent(String[] words, int k) {
        //Build Frequency Lookup Table
        for (String word: words) {
            if (!wordToFreq.containsKey(word)) 
                wordToFreq.put(word, 0);
            wordToFreq.put(word, 1+wordToFreq.get(word));
            maxFreq = Math.max(maxFreq, wordToFreq.get(word));
        }
        
        //Build Frequency to Words Table.
        for (int i = 0; i <= maxFreq; i++) { //freqToWords[0] will not be used
            freqToWords.add(new TreeSet<String>());
        }
        for (String word: words) {
            freqToWords.get(wordToFreq.get(word)).add(word);
        }
           
        //Build Result;
        List<String> result = new ArrayList<>();
        int count = 0;
        for (int freq = maxFreq; freq > 0; freq--) {
            TreeSet<String> candidates = freqToWords.get(freq);
            
            for (Iterator<String> it = candidates.iterator(); it.hasNext();) {
                result.add(it.next());
                count++;
                if (count == k) return result;
            }
        }
        return result;
    }
}
```
## [78. Subsets](https://leetcode.com/problems/subsets/description/)

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> results = new LinkedList<>();        
        backtrack(nums, 0, new ArrayList<>(), results);     
        return results;
    }
    
    private void backtrack(int[] nums, int start, List<Integer> prefix, List<List<Integer>> results) {
        results.add(new ArrayList<>(prefix));
        for (int i = start; i < nums.length; i++) {
            prefix.add(nums[i]);
            backtrack(nums, i+1, prefix,results);
            prefix.remove(prefix.size()-1);
        }
    }
}
```

## [15. 3Sum](https://leetcode.com/problems/3sum/description/)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

```java
public class Solution {
    //O(N ^ 2)
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length < 3) return result;
        
        //A solution looks like [num[i], num[j], num[k]] 
        Arrays.sort(nums); //O(N log N)
        for(int i = 0; i < nums.length - 2;) { 
            //i: the smallest index must be less than 0 for the sum to be zero
            if (nums[i] > 0) break;
            
            //j: starts from i+1, and k starts from back
            int j = i + 1;
            int k = nums.length - 1;
            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                if (sum <= 0) while(nums[j]==nums[++j] && j < k); //skip equal nums[j] values
                if (sum >= 0) while(nums[k--] == nums[k] && j < k); //skip equal nums[k] values
            }
            while(nums[i]==nums[++i] && i < nums.length - 2); //skip equal nums[i] values
        }
        return result;
    }
}
```

## [535. Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)

Note: This is a companion problem to the [System Design](https://leetcode.com/problemset/system-design/) problem: [Design TinyURL](https://leetcode.com/problems/design-tinyurl/).

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
```
public class Codec {
    private static int timer = 0;
    private static String generateTinyUrl() {
        return Integer.toString(timer++);
    }
    private HashMap<String, String> short2long = new HashMap<>();
    private HashMap<String, String> long2short = new HashMap<>();
    
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String shortUrl = generateTinyUrl();
        short2long.put(shortUrl, longUrl);
        long2short.put(longUrl, shortUrl);
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return short2long.get(shortUrl);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
```

## [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/description/)

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

```java
class Solution {
    //Reverse char[begin...end)
    public void reverse(char[] str, int begin, int end) {
        for (int i = begin, j = end - 1; i < j; i++, j--) {
            char tmp = str[i];
            str[i] = str[j];
            str[j] = tmp;
        }
    }
    public void reverseWords(char[] str) {
        //Reverse entire string
        reverse(str, 0, str.length);
        System.out.println(str);
        
        //Reverse each word in the string
        for (int begin = 0, end = 0; end <= str.length; end++) {
            if (end < str.length && str[end] != ' ') continue;
            reverse(str, begin, end);
            begin = end+1;
        }
    }
}
```

## [529. Minesweeper](https://leetcode.com/problems/minesweeper/description/)

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example 1:
```
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
```
Explanation:

![alt text](https://leetcode.com/static/images/problemset/minesweeper_example_1.png)

Example 2:
```
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
```
Explanation:
![alt text](https://leetcode.com/static/images/problemset/minesweeper_example_2.png)

Note:
* The range of the input matrix's height and width is [1,50].
* The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one * clickable square.
* The input board won't be a stage when game is over (some mines have been revealed).
* For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

```java
class Solution {
    
    private char[] int2char = new char[] {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    
    public char[][] updateBoard(char[][] board, int[] click) {
        int I = click[0], J = click[1];
        
        //Rule 1: If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if (board[I][J] == 'M') {
            board[I][J] = 'X';
            return board;
        }
        
        //Rule 2, 3: DFS
        boolean[][] marked= new boolean[board.length][board[0].length];
        if (board[I][J] == 'E') {
            updateBoard(board, I, J, marked); 
        }
        return board;
    }
    
    private void updateBoard(char[][] board, int I, int J, boolean[][] marked) {
        if (I < 0 || I >= board.length || J < 0 || J >= board[0].length) return;
        
        if (marked[I][J] == true) return;
        else marked[I][J] = true;
        
        if (board[I][J] == 'E') {
            int bombs = peekBombs(board, I, J);
            if (bombs == 0) {
                //Rule 2
                board[I][J] = 'B';
                updateBoard(board, I-1, J-1, marked);
                updateBoard(board, I-1, J, marked);
                updateBoard(board, I-1, J+1, marked);
                updateBoard(board, I, J-1, marked);
                updateBoard(board, I, J+1, marked);
                updateBoard(board, I+1, J-1, marked);
                updateBoard(board, I+1, J, marked);
                updateBoard(board, I+1, J+1, marked);
                
            } else {
                //Rule 3
                board[I][J] = int2char[bombs];
            }
        } 
    }
    
    private int peekBombs(char[][] board, int I, int J) {
        return 
            bombCountHelper(board, I-1, J-1) + 
            bombCountHelper(board, I-1, J) + 
            bombCountHelper(board, I-1, J+1) + 
            bombCountHelper(board, I, J-1) +
            bombCountHelper(board, I, J+1) + 
            bombCountHelper(board, I+1, J-1) + 
            bombCountHelper(board, I+1, J) + 
            bombCountHelper(board, I+1, J+1); 
    }
    
    private int bombCountHelper(char[][] board, int I, int J) {
        if (I < 0 || I >= board.length || J < 0 || J >= board[0].length) return 0;
        return board[I][J] == 'M' || board[I][J] == 'X' ? 1 : 0;
    }
}
```

725. Split Linked List in Parts
DescriptionHintsSubmissionsDiscussSolution
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
```
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
```

Example 2:
```
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```
Note:

* The length of root will be in the range [0, 1000].
* Each value of a node in the input will be an integer in the range [0, 999].
* k will be an integer in the range [1, 50].

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
    public ListNode[] splitListToParts(ListNode root, int k) {
        //Step 1: Count total size of list
        int size = 0;
        for (ListNode runner = root; runner != null; runner = runner.next) size++;
        
        //Step 2: Split the parts based on calculation: 
        //After split:
        //  - The first remainder lsit should have size of k+1;
        //  - The rest should have size of k;
        int quote = size / k;
        int remainder = size % k;
        System.out.println(quote + " " + remainder);
        ListNode[] result = new ListNode[k];
        ListNode runner = root;
        for (int i = 0; i < k; i++) {
            result[i] = runner;
            //For Case where k > size of the list
            if (quote > 0) {
                //Step 2.1: Advance quote step
                for (int j = 0; j < quote - 1; j++) {
                    runner = runner.next;
                 }
            
                //Step 2.2: Advance one step more if [0, remainer) to have size of quote + 1
                if (i < remainder) {
                    System.out.println("Remainder ");
                    runner = runner.next;
                }
            }
            
            //Step 2.3: Break current list
            if (runner != null) {
                ListNode next = runner.next;
                runner.next = null;
                runner = next;
            }
        }
        return result;
    }
}
```

## 516. Longest Palindromic Subsequence
DescriptionHintsSubmissionsDiscussSolution
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
```
Input:
"bbbab"
Output:
4
```
One possible longest palindromic subsequence is "bbbb".

Example 2:
```
Input:
"cbbd"
Output:
2
```
One possible longest palindromic subsequence is "bb".

```java
class Solution {
    /*
    Dynamic Programming
    
    For example: for string "abbca", we create the count array as follow
    
    //Count[begin][end] counts the longestPalindromeSubseq for string [begin, end)
    //The underlying string representation looks like below
        a     ab    abb   abbc  abbca
        null  b     bb    bbc   bbca
        null  null  b     bc    bca
        null  null  null  c     ca
        null  null  null  null  a     <== start from this corner
        
    //BEGIN start from bottom line
             a b b c a
          a  0 0 0 0 0       Go Up 
          b  0 0 0 0 0          ^
          b  0 0 0 0 0          |
          c  0 0 0 0 0  
          a  0 0 0 0 1  <-   begin  

        
    //Then move one row up, END starts from BEGIN
             a b b c a
          a  0 0 0 0 0       Go Up 
          b  0 0 0 0 0          ^
          b  0 0 0 0 0          |
          c  0 0 0 1 0  <===   begin (end -> Go Right)
          a  0 0 0 0 1   
          
    //Finally the matrix will look like this
             a b b c a
          a  1 1 2 2 4       Go Up 
          b  0 1 2 2 2          ^
          b  0 0 1 1 1          |
          c  0 0 0 1 1  <===   begin (end -> Go Right)
          a  0 0 0 0 1   
        
    */
        
    public int longestPalindromeSubseq(String s) {
        int[][] dp = new int[s.length()][s.length()];
        if (s.length() < 2) return s.length();
        for (int begin = s.length() - 1; begin >= 0; begin--) {
            dp[begin][begin] = 1;
            for (int end = begin + 1; end < s.length(); end++) {
                if (begin > s.length() - 2 || end < 1) continue;
                
                if (s.charAt(begin) == s.charAt(end)) {
                    dp[begin][end] = dp[begin+1][end-1] + 2;
                } else {
                    dp[begin][end] = Math.max(dp[begin+1][end], dp[begin][end-1]);
                }
            }
        }
        return dp[0][s.length()-1];
    }
}
```

## 73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


Follow up:
* Did you use extra space?
* A straight forward solution using O(mn) space is probably a bad idea.
* A simple improvement uses O(m + n) space, but still not the best solution.
* Could you devise a constant space solution?

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        boolean firstRowContainsZero = false;
        boolean firstColContainsZero = false;
        
        int M = matrix.length;
        int N = matrix[0].length;
        
        //Use First Row and First Col to indicate the row/col to be cleared
        //Save the original first Row/Col zeroness with a flag
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0) firstRowContainsZero = true;
                    if (j == 0) firstColContainsZero = true;
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        //Clear up the marked Row/Col
        for (int i = 1; i < M; i++) { //<== Skip First Row
            for (int j = 1; j < N; j++) { //<=== Skip First Col
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        } 
        
        //If original first Row contains 0 , clear first Row
        if(firstRowContainsZero) {
            for(int j = 0; j < N; j++) {
                matrix[0][j] = 0;
            }
        }
        
        
        //If original first Col contains 0 , clear first Col
        if(firstColContainsZero) {
            for(int i = 0; i < M; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```
## [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
```
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
You should return [1, 3, 4].


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
    //Travel Layer by Layer and record the last node in each layer
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        
        queue.offer(root);
        while (!queue.isEmpty()){
            int count = queue.size(); //Number of nodes at this layer
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
                if (i == count - 1) result.add(node.val);
            }
        }
        
        return result;
    }
}
```

## [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

```java
//Use double to store result temporarily to prevent overflow/underflow
class Solution {
    public int myAtoi(String str) {
        if (str.length() == 0) return 0;
        
        double result = 0;
        int i = 0;
        boolean negativeFlag = false;
        
        //Skip whitespace "   123"
        while (i < str.length() && str.charAt(i) == ' ') {
            i++;
        }
        
        //Read sign: consider "++---+++123"
       if (str.charAt(i) == '-' || str.charAt(i) == '+') {
            negativeFlag = str.charAt(i) == '-' ? !negativeFlag : negativeFlag;
            i++;
        }
        
        //Parse number
        while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            result = result * 10 + str.charAt(i) - '0';
            i++;
        }
        
        //Form the result in double and return MAX_INT/MIN_INT if over boundary
        result *= negativeFlag ? -1 : 1;
        if (result <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
        if (result >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
        return (int)result;
    }
}
```

##  [89. Gray Code](https://leetcode.com/problems/gray-code/description/)

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
```
00 - 0
01 - 1
11 - 3
10 - 2
```
Note:

For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

```java
public class Solution {
    // i XOR (i/2)
    public List<Integer> grayCode(int n) {
        List<Integer> result = new LinkedList<>();
        for (int i = 0; i < 1<<n; i++) result.add(i ^ i>>1); // i XOR (i/2)
        System.out.println(result);
        return result;
    }
}
```

```
/*
Recursion: Running Stack when N = 3

GRAY <N: 3>, <Prefix: >
    GRAY <N: 2>, <Prefix: 0>
        GRAY <N: 1>, <Prefix: 00>
            GRAY <N: 0>, <Prefix: 000>
            YARG <N: 0>, <Prefix: 001>
        YARG <N: 1>, <Prefix: 01>
            GRAY <N: 0>, <Prefix: 011>
            YARG <N: 0>, <Prefix: 010>
    YARG <N: 2>, <Prefix: 1>.
        GRAY <N: 1>, <Prefix: 11>
            GRAY <N: 0>, <Prefix: 110>
            YARG <N: 0>, <Prefix: 111>
        YARG <N: 1>, <Prefix: 10>
            GRAY <N: 0>, <Prefix: 101>
            YARG <N: 0>, <Prefix: 100>
*/

public class Solution {
    // append reverse of order n gray code to prefix string
    private static void yarg(String prefix, int n, List<Integer> result) {
        //System.out.println("YARG <N: " + n +">, <Prefix: " + prefix +">");
        if (n == 0) result.add(Integer.parseInt(prefix, 2));
        else {
            gray(prefix + "1", n - 1, result);
            yarg(prefix + "0", n - 1, result);
        }
    }  

    // append order n gray code to end of prefix string
    private static void gray(String prefix, int n, List<Integer> result) {
        //System.out.println("GRAY <N: " + n +">, <Prefix: " + prefix +">");
        if (n == 0) result.add(Integer.parseInt(prefix, 2));
        else {
            gray(prefix + "0", n - 1, result);
            yarg(prefix + "1", n - 1, result);
        }
    }  

    public List<Integer> grayCode(int n) {
        List<Integer> result = new LinkedList<>();
        if (n == 0) return result;
        else gray("", n, result);
        return result;
    }
}
```

## [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/description/)

Given a string, sort it in decreasing order based on the frequency of characters.
```
Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

Example 2:
```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

Example 3:
```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```


```java
class Solution {
    public String frequencySort(String s) {
        int maxFreq = 0;
        int[] map = new int[128];
        //Count frequency O(N)
        for (char c: s.toCharArray()) {
            map[c]++;
        }
        
        //Build reverse lookup O(N)
        Map<Integer, List<Character>> freqToChars = new HashMap<>();
        for (char c = 0; c < map.length; c++) {
            int freq = map[c];
            if (freq > 0) {
                maxFreq = Math.max(maxFreq, freq);
                if (!freqToChars.containsKey(freq)) 
                    freqToChars.put(freq, new ArrayList<Character>());
                freqToChars.get(freq).add(c);
            }
        }
        
        //Build return result O(N)
        StringBuilder sb = new StringBuilder();
        for (int freq = maxFreq; freq > 0; freq--) {
            if (freqToChars.containsKey(freq)) {
                for (char c: freqToChars.get(freq)) {
                    for (int i = 0; i < freq; i++) {
                        sb.append(c);
                    }
                }
            }
        }
        return sb.toString();
    }
}
```
## [508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/description/)

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
```
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
```

Examples 2
```
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
```

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

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
    private Map<TreeNode, Integer> treeToSum = new HashMap<>();
    private Map<Integer, Integer> sumToFreq = new HashMap<>();
    private Map<Integer, List<Integer>> freqToSums = new HashMap<>();
    
    public int[] findFrequentTreeSum(TreeNode root) {
        if (root == null) return new int[0];
        
        //Build treeToSum map
        getSubTreeSum(root);
        
        //Build sumToFreq
        for (int sum: treeToSum.values()) {
            if (!sumToFreq.containsKey(sum)) 
                sumToFreq.put(sum, 0);
            sumToFreq.put(sum, sumToFreq.get(sum) + 1);
        }
                        
        //Build freqToSums
        for (int sum: sumToFreq.keySet()) {
            int freq = sumToFreq.get(sum);
            if (!freqToSums.containsKey(freq)) 
                freqToSums.put(freq, new LinkedList<>());
            freqToSums.get(freq).add(sum);
        }
        
        //Get max freq and Return result as int[]
        int maxFreq = Collections.max(sumToFreq.values());
        return freqToSums.get(maxFreq).stream()
                          .mapToInt(Integer::intValue)
                          .toArray();
            
    }
    
    private int getSubTreeSum(TreeNode node) {
        if (node == null) return 0;
        if (treeToSum.containsKey(node)) return treeToSum.get(node);
        int sum = node.val + getSubTreeSum(node.left) + getSubTreeSum(node.right);
        treeToSum.put(node, sum);
        return sum;
    }
}
```
## [204. Count Primes](https://leetcode.com/problems/count-primes/description/)

Description:

Count the number of prime numbers less than a non-negative number, n.

```java
class Solution {
    public int countPrimes(int n) {
        boolean[] notPrime = new boolean[n];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i] == false) { // Prime Number
                count++;
                for (int j = 2; i * j < n; j++) {
                    notPrime[i*j] = true;
                }
            }
        }
        return count;
    }
}
```

## 414. Third Maximum Number
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
```
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```

Example 2:
```
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```

Example 3:

```
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
````

```java
class Solution {
    public int thirdMax(int[] nums) {
        //Primitive type cannot be converted to collections directly, must first box to object
        Integer[] wrapper = Arrays.stream(nums).boxed().toArray(Integer[]::new); 
        Set<Integer> numSet = new HashSet<Integer>(Arrays.asList(wrapper));
        
        //Return max if less than 3 unique number
        if (numSet.size() < 3) return Collections.max(numSet);
        
        //Otherwise return the third maximum
        PriorityQueue<Integer> heap = new PriorityQueue<>(3);
        for (int num: numSet) {
            if (heap.size() >= 3 && heap.peek() < num) {
                heap.poll();
            }
            
            if (heap.size() < 3) {
                heap.offer(num);
            } 
        }
        return heap.peek();
    }
}
```
## [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/description/)

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
```
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
```

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
//Based on the property of BST, all the right descendant on the right must be greater than the node
//all the left descendant on the left must be less than the node
//Therefore: always visti right child first, then root value adds the right child value, then the left child add root value
public class Solution {
    int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        if (root == null) return root;
        convertBST(root.right);
        root.val += sum;
        sum = root.val;
        convertBST(root.left);
        return root;
    }
}
```

## [189 Rotate Array](https://leetcode.com/problems/rotate-array/description/)

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?

```java
/*
This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-k elements gives us the required result.

Let n=7 and k=3.

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

*/
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k , nums.length - 1);
    }
    
    public void reverse(int[] nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
```
## [355. Design Twitter](https://leetcode.com/problems/design-twitter/description/)

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

1. postTweet(userId, tweetId): Compose a new tweet.
2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
3. follow(followerId, followeeId): Follower follows a followee.
4. unfollow(followerId, followeeId): Follower unfollows a followee.

Example:
```
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
```
```java
public class Twitter {

    private static int TIMESTAMP = 0;
    private HashMap<Integer, User> uid2User;
    
    public class Tweet {
        private int id;
        private int timestamp;
        private Tweet next;
        
        public Tweet(int id) {
            this.id = id;
            this.timestamp = TIMESTAMP++;
            this.next = null;
        }
        
        public int id() {
            return id;
        }
        
        public Tweet next() {
            return next;
        }
        
        public int timestamp() {
            return timestamp;
        }
        
    }
    
    public class User {
        private int userId;
        private Set<Integer> following; //A set of uid current user is following
        private Tweet tweet_head;
        
        public User(int id) {
            this.userId = id;
            following = new HashSet<Integer>();
            following.add(id); //Follows self
            tweet_head = null;
        }
        
        public void follow(int uid) {
            following.add(uid);
        }
        
        public void unfollow(int uid) {
            if (following.contains(uid))
                following.remove(uid);
        }
        
        public void post(int tid) {
            Tweet t = new Tweet(tid);
            t.next = tweet_head;
            tweet_head = t;
        }
        
        //Return all userId I'm following
        public Set<Integer> following() {
            return following;
        } 
        
        //Return the latest tweet
        public Tweet latest() {
            return tweet_head;
        }
    }
    
    /** Initialize your data structure here. */
    public Twitter() {
        uid2User = new HashMap<>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        if (!uid2User.containsKey(userId)) {
            uid2User.put(userId, new User(userId));
        }
        uid2User.get(userId).post(tweetId);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> result = new LinkedList<>();
        if (!uid2User.containsKey(userId)) return result;
        
        Set<Integer> followings = uid2User.get(userId).following(); //The list of UID current user is following
        PriorityQueue<Tweet> heap = new PriorityQueue<>(followings.size(), (a,b) -> b.timestamp() - a.timestamp()); //MAX heap
	//Put each following user's latest tweet in the heap
        for (int uid: followings) {
            Tweet latest = uid2User.get(uid).latest();
            if (latest != null) { //Make sure the latest tweet is not null!
                heap.offer(latest);
            }
        }
        
        //We will try to get 10 tweets from the heap
        //Whenever we choose a tweet, we will put the selected user's next tweet into the heap
        int count = 0;
        while (!heap.isEmpty() && count < 10) {
            Tweet latest = heap.poll();
            result.add(latest.id());
            count++;
            if (latest.next() != null) {
                heap.offer(latest.next());
            }
        }
        return result;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if (!uid2User.containsKey(followerId)) {
            uid2User.put(followerId, new User(followerId));
        }
        
        if (!uid2User.containsKey(followeeId)) {
            uid2User.put(followeeId, new User(followeeId));
        }
        uid2User.get(followerId).follow(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if (!uid2User.containsKey(followerId) || followeeId == followerId) {
            return;
        }
        uid2User.get(followerId).unfollow(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
 ```

## [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/description/)

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
```
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
```
Note: The merging process must start from the root nodes of both trees.

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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null) return t2;
        if (t2 == null) return t1;
        
        //A exploring queue for tuplet <currentTree, t1 TreeNode, t2 TreeNode>
        Queue<TreeNode[]> queue = new LinkedList<>(); 
        
        TreeNode root = createTreeNode(t1, t2);
        queue.offer(new TreeNode[]{root, t1, t2});
        
        while (!queue.isEmpty()) {
            TreeNode[] nodes = queue.poll(); //nodes[0]=currentNode, nodes[1]=t1Node, nodes[2]=t2Node
            TreeNode current = nodes[0], node1 = nodes[1], node2 = nodes[2];

            //Skip null node in current tree
            if (current == null) continue;
            
            //Create Left Child for current node
            TreeNode left1 = node1 == null ? null : node1.left; //Left child of node in t1
            TreeNode left2 = node2 == null ? null : node2.left; //Left child of node in t2
            current.left = createTreeNode(left1, left2);
            
            //Create Right Child for current node
            TreeNode right1 = node1 == null ? null : node1.right; //Right child of node in t1
            TreeNode right2 = node2 == null ? null : node2.right; //Right child of node in t2
            current.right = createTreeNode(right1, right2);
            
            //Enqueue left and right
            queue.offer(new TreeNode[]{current.left, left1, left2});
            queue.offer(new TreeNode[]{current.right, right1, right2});
        }
        
        return root;
    }
    
    private TreeNode createTreeNode(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        int val1 = t1 == null ? 0 : t1.val;
        int val2 = t2 == null ? 0 : t2.val;
        
        return new TreeNode(val1 + val2);
    }
}
```

## [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/description/)

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
```
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```
Example 2:
```
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```
Example 3:
```
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

Note:

1. The pairs (i, j) and (j, i) count as the same pair.
2. The length of the array won't exceed 10,000.
3. All the integers in the given input belong to the range: [-1e7, 1e7].

```java
class Solution {
    public int findPairs(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 0) return 0;
        
        //Build a number frequency map
        Map<Integer, Integer> numFreq = new HashMap<>();
        for (int num: nums) {
            numFreq.put(num, numFreq.getOrDefault(num, 0) + 1);
        }
        
        int counts = 0;
        if (k == 0) { //When k is 0, find the number that appears at least twice
            for (int value: numFreq.values()) {
                if (value >= 2)
                    counts++;
            }
        } else { //Otherwise, for each num, see if num+k is also in the table
            for (int num: numFreq.keySet()) {
                if (numFreq.containsKey(num+k)) {
                    counts++;
                }
            }
        }
        
        return counts;
    }
}
```

## [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

```java
class Solution {
    //The Nth Row in in Pascal triangle will be
    //C(N, 0), C(N, 1), C(N, 2) ... C(N, N-1), C(N, N)
    //Use the Combinatics formula we know that
    //  - C(N, k) == C(N, N-k);
    //  - C(N, k) = N! / ((N-i)!*N!)
    public List<Integer> getRow(int rowIndex) {
        int N = rowIndex;
        Integer[] result = new Integer[N+1];
        
        for (int i = 0; i < N/2+1; i++) {
            result[i] = C(N, i);
            result[N-i] = result[i]; //C(N, k) == C(N, N-k);
        }
        return Arrays.asList(result);
    }
    
    //Divide as soon as possible in case of overflow
    protected int C(int base, int i) {
        double result = 1;
        for (int j=0; j<i; j++) {   //C(N, k) = N! / ((N-i)!*N!)
            result *= (base-j);     //Computes Numerator: N!/(N-k)!
            result /= (j+1);        //Computes Denominator: k!
        }
        return (int)result;
    }

}
```

## [536. Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/description/)

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
```
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
```
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

**Ike's Comment: Read the [Simple Python Interpreter](https://github.com/cookieisaac/interpreter), especially part 5 and part 7**

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
//A Tree Compiler: Idea from https://github.com/cookieisaac/interpreter
// - User Lexer to turn char stream to token stream
// - User parser to evaluate token stream
public class Solution {
    protected enum TokenType {
        INTEGER,
        LPAREN,     //Left Parenthesis
        RPAREN,     //Right Rarenthesis
        EOF
    }
    
    public class Token {
        TokenType   type;
        Object      value;
        
        public Token(TokenType type, Object value) {
            this.type = type;
            this.value = value;
        }
    }
    
    //Text Stream -> Token Stream
    protected class Lexer {
        private String text;
        private int position;
        private char currentChar;
        private static final char END = '#';
        
        public Lexer(String text) {
            this.text = text;
            position = 0;
            currentChar = text.charAt(position);
        }
    
        //Advacne the position pointer and set currentChar
        private void advance() {
            position += 1;
            if (position == text.length()) {
                currentChar = END; //Indicates end of input
            } else {
                currentChar = text.charAt(position);
            }
        }

        public Integer integer() {
            StringBuilder sb = new StringBuilder();
            while (currentChar != END && (currentChar == '-' || Character.isDigit(currentChar))) {
                sb.append(currentChar);
                advance();
            }
            return Integer.parseInt(sb.toString());
        }
        
        public Token getNextToken() {
            while (currentChar != END) {
                if (currentChar == '(') {
                    advance();
                    return new Token(TokenType.LPAREN, '(');
                } else if (currentChar == ')') {
                    advance();
                    return new Token(TokenType.RPAREN, ')'); 
                } else if (Character.isDigit(currentChar) || currentChar == '-'){
                    return new Token(TokenType.INTEGER, integer());
                }
            }
            return new Token(TokenType.EOF, null);
        }
    }
    
    //Token Stream -> evaluated result
    protected class Parser {
        private Lexer lexer;
        private Token currentToken;
        
        public Parser(Lexer lexer) {
            this.lexer = lexer;
        }
        
        public TreeNode getTree() {
            Stack<TreeNode> parentStack = new Stack<>(); //A stack for all parent TreeNode
            for (Token currentToken = lexer.getNextToken(); 
                 currentToken.type != TokenType.EOF; 
                 currentToken = lexer.getNextToken()) {
                switch (currentToken.type) {
                    case RPAREN: //No more children for the node sitting at stack top
                        parentStack.pop();
                        break;
                    case INTEGER: //Create TreeNode and attach to parent
                        TreeNode node = new TreeNode((Integer)currentToken.value);
                        if (!parentStack.isEmpty()) {
                            TreeNode parent = parentStack.peek();
                            if (parent.left != null) parent.right = node;
                            else parent.left = node;
                        }
                        parentStack.push(node);
                        break;
                    case LPAREN:
                        break;
                }
            }
            return parentStack.isEmpty() ? null : parentStack.peek();
        }
    }
    
    public TreeNode str2tree(String s) {
        if (s.equals("")) return null;
        
        Lexer lexer = new Lexer(s);
        Parser parser = new Parser(lexer);
        return parser.getTree();
    }
}
```

## [537. Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/description/)

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
```
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

Example 2:
```
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

Note:
* The input strings will not have extra blank.
* The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

```java
class Solution {
    protected class ComplexNumber {
        protected int imag;
        protected int real;
        
        private int parseInt(String str) {
            if (str.contains("i")) return Integer.parseInt(str.substring(0, str.length()-1));
            else return Integer.parseInt(str);
        }

        public ComplexNumber(String str) {
            String[] splitted = str.split("\\+"); //Split string by plus sign
            real = parseInt(splitted[0]);
            imag = parseInt(splitted[1]);  
        }
        
        public ComplexNumber(int real, int imag) {
            this.imag = imag;
            this.real = real;
        }

        public ComplexNumber multiply(ComplexNumber other) {
            return new ComplexNumber(
                this.real*other.real - this.imag*other.imag,
                this.real*other.imag + this.imag*other.real
            );
        }
        
        public String toString() {
            return real+"+"+imag+"i";
        }
    }
    
    public String complexNumberMultiply(String a, String b) {
        ComplexNumber A = new ComplexNumber(a);
        ComplexNumber B = new ComplexNumber(b);
        
        return A.multiply(B).toString();
    }
}
```

## [553. Optimal Division](https://leetcode.com/problems/optimal-division/description/)

Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:
```
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
```
Note:

1. The length of the input array is [1, 10].
2. Elements in the given array will be in range [2, 1000].
3. There is only one optimal division for each test case.

```java
class Solution {
    /* 
         X1/X2/X3/…/Xn will always be equal to (X1/X2) * Y, no matter how you place parentheses. 
         i.e no matter how you place parentheses, X1 always goes to the numerator and X2 always goes to the denominator. 
         
         Hence you just need to maximize Y. 
         And Y is maximized when it is equal to X3 *…*Xn. 
         
         So the answer is always X1/(X2/X3/…/Xn), which is (X1 *X3 *…*Xn)/X2
    */
    public String optimalDivision(int[] nums) {
        StringBuilder builder = new StringBuilder();
        builder.append(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (i==1 && nums.length > 2) {
                builder.append("/(").append(nums[i]);
            } else {
                builder.append("/").append(nums[i]);
            }
        }
        return nums.length > 2 ? builder.append(")").toString(): builder.toString();
    }
}
```

## [579. Find Cumulative Salary of an Employee](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/description/)

The Employee table holds the salary information in a year.

Write a SQL to get the cumulative sum of an employee's salary over a period of 3 months but exclude the most recent month.

The result should be displayed by 'Id' ascending, and then by 'Month' descending.

Example
Input
```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
```
Output
```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
```
Explanation

Employee '1' has 3 salary records for the following 3 months except the most recent month '4': salary 40 for month '3', 30 for month '2' and 20 for month '1'
So the cumulative sum of salary of this employee over 3 months is 90(40+30+20), 50(30+20) and 20 respectively.

```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
```
Employee '2' only has one salary record (month '1') except its most recent month '2'.
```
| Id | Month | Salary |
|----|-------|--------|
| 2  | 1     | 20     |
```
Employ '3' has two salary records except its most recent pay month '4': month '3' with 60 and month '2' with 40. So the cumulative salary is as following.
```
| Id | Month | Salary |
|----|-------|--------|
| 3  | 3     | 100    |
| 3  | 2     | 40     |
```

```sql
/*
Explanation:
`FROM Employee A, Employee B WHERE A.Id = B.Id` is self join which would report all possible “month” combinations of records for the same employee.

A.Id    A.Month     A.Salary    B.Id    B.Month     B.Salary
1       1           20          1       1           20
1       1           20          1       2           30
1       1           20          1       3           40
1       1           20          1       4           60
1       1           20          1       5           70
1       2           20          1       1           20
1       2           20          1       2           30
etc

We want to aggregate salary over 3 months before the reported month. In the above example for EmployeeId = 0 and month 5 we want aggregate salary for months 2, 3, and 4:
A.month : 5 => B.month : 4, 3, 2
A.month : 4 => B.month : 3, 2, 1
A.month : 3 => B.month : 2, 1
A.month : 2 => B.month : 1

which is done with
`SELECT SUM(B.Salary) as Salary
WHERE B.Month BETWEEN(A.Month - 3) AND (A.Month - 1)` <<< for example months 4, 3 and 2 are between 5-3 and 5-1

Finally, we want to report the last month of those records included in the SUM(B.Salary),
rather than A.Salary which is done with SELECT MAX(B.Month). <<< for example for A.month = 5 it will select max(4, 3, 2) or 4

*/
SELECT   A.Id, MAX(B.Month) as Month, SUM(B.Salary) as Salary
FROM     Employee A, Employee B
WHERE    A.Id = B.Id AND B.Month BETWEEN (A.Month-3) AND (A.Month-1)
GROUP BY A.Id, A.Month
ORDER BY Id, Month DESC
```

## [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/)

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
```
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
```
Example 2:
```
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
```
```
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
    //The parenthsis of around the value is set by the parent only
    public String tree2str(TreeNode node) {
        if (node == null) return "";//Empty Node
        if (node.left == null && node.right == null) return Integer.toString(node.val);//Leaf Node
        if (node.right == null) return node.val+"("+ tree2str(node.left)+")";//Node without right child
        if (node.left == null) return node.val+"()"+"(" + tree2str(node.right) + ")";//Node without left child
        return node.val+ "(" + tree2str(node.left)+")("+tree2str(node.right)+")";//Regular Node
    }
}
```

## [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
```
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
```
Example 2:
```
Input: "aba"

Output: False
```
Example 3:
```
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```

```java
class Solution {
    public boolean repeatedSubstringPattern(String str) {
        int L = str.length();
        
        //String length doesn't have to be even, for example "aaa" will be true  
        //NOTE: check must be p <= L, not p < L, this will take care the case of "bb"
        for (int p = 2; p <= L ;p++) { 
            //Try to break str into p parts
            //If str can't break into p parts, try p+1 parts
            if (L % p != 0) continue; 
            
            //If str can break into p parts, then each part is of length l
            //Then repeat this substring p times, and see if it's the same as original string
            int l = L/p;              
            String sub = str.substring(0, l);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < p; i++) sb.append(sub);
            System.out.println(sb.toString());
            if (str.equals(sb.toString())) return true;
        }
        return false;
    }
}
```

## [640. Solve the Equation](https://leetcode.com/problems/solve-the-equation/description/)

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
```
Input: "x+5-3+x=6+x-2"
Output: "x=2"
```
Example 2:
```
Input: "x=x"
Output: "Infinite solutions"
```
Example 3:
```
Input: "2x=x"
Output: "x=0"
```
Example 4:
```
Input: "2x+3x-6x=x+2"
Output: "x=-1"
```
Example 5:
```
Input: "x=x+2"
Output: "No solution"
```

```java
public class Solution {
    public enum TokenType {
        PLUS,
        MINUS,
        X,
        COEF, //Coefficient
        INTEGER, //Integer
        EOF //End of file   
    }
    
    public class Token {
        private TokenType   type;
        private Object      value;
        
        public Token(TokenType type, Object value) {
            this.type = type;
            this.value = value;
        }
        
        public TokenType type() {return type;}
        public Object value() {return value;}
        public void setValue(int value) { this.value = value; }
        public String toString() { return "("+type+","+value+")"; }
    }
    
    public class Lexer {
        private String text;
        private int position;
        private char currentChar;
        private static final char END = '#';
        
        public Lexer(String text) {
            this.text = text;
            position = 0;
            currentChar = text.length() == 0 ? END: text.charAt(0);
        }
        
        //Parse text stream to token stream
        public Token getNextToken() {
            while (currentChar != END) {
                if (currentChar == '+') {
                    advance();
                    return new Token(TokenType.PLUS, '+');
                } else if (currentChar == '-') {
                    advance();
                    return new Token(TokenType.MINUS, '-');
                } else if (currentChar == 'x') {
                    advance(); //If the character is x, it will generate a coeff of 1
                    return new Token(TokenType.COEF, 1);
                } else if (Character.isDigit(currentChar)) {
                    int value = integer();
                    if (peek() == 'x') {
                        advance(); ////e.g.: x+2x, this will capture 2x but failed to capture 1x, since no digit was ahead of x
                        return new Token(TokenType.COEF, value);
                    } else {
                        return new Token(TokenType.INTEGER, value);
                    }
                } 
            }
            return new Token(TokenType.EOF, null);
        }
        
        private void advance() {
            position+=1;
            if (position >= text.length()) {
                currentChar = END;
            } else {
                currentChar = text.charAt(position);
            }
        }
        
        private char peek() {
            return currentChar;
        }
        
        private Integer integer() {
            StringBuilder sb = new StringBuilder();
            while (Character.isDigit(currentChar)) {
                sb.append(currentChar);
                advance();
            }
            return Integer.parseInt(sb.toString());
        }
    }
    
    public class Parser {
        private Lexer lex;
        private ArrayList<Token> coefs;
        private ArrayList<Token> values;
        
        public Parser(Lexer lex) {
            this.lex = lex;
            this.coefs = new ArrayList<Token>();
            this.values = new ArrayList<Token>();
            parse();
        }
        
        //Understand the syntax of the formula
        private void parse() {
            int sign = 1; //Use this to indicate previous token is PLUS/MINUS
            for (Token token = lex.getNextToken(); token.type != TokenType.EOF; token = lex.getNextToken()) {
                switch(token.type) {
                    case PLUS: sign = 1; break;
                    case MINUS: sign = -1; break;
                    case COEF://COEF will consume the PLUS and MINUS sign
                        token.setValue((Integer)token.value()*sign);
                        coefs.add(token);
                        sign = 1; //Reset sign after consumption
                        break;
                    case INTEGER:
                        token.setValue((Integer)token.value()*sign);
                        values.add(token);
                        sign = 1;//Reset sign since it's consumed already
                        break;
                    case X:
                        break;
                }
            }
            //System.out.println("Coefs:" + coefs);
            //System.out.println("Values:" + values);
        }
        
        public Integer getCoef() {
            Integer result = 0;
            for (Token token: coefs) {
                result += (Integer)token.value;
            }
            return result;
        }
        
        public Integer getValue() {
            Integer result = 0;
            for (Token token: values) {
                result += (Integer)token.value;
            }
            return result;
        }
    }
    
    public String solveEquation(String equation) {
        String[] sides = equation.split("=");
        Parser lhs = new Parser(new Lexer(sides[0])); //Left hand side
        Parser rhs = new Parser(new Lexer(sides[1])); //Right hand side
        
        int coef = lhs.getCoef() - rhs.getCoef();
        int value = rhs.getValue() - lhs.getValue();
        
        if (coef == 0 && value == 0) { // e.g.: x=x
            return "Infinite solutions";
        } else if (coef == 0) { //e.g.: x=x+1
            return "No solution";
        } else { //e.g.: 2x=4
            return "x="+Integer.toString(value/coef);
        }
    }
}
```

## [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/description/)

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

```java
//O(N) time, O(1) space
class Solution {
    /*
    If you had an extra array, you will visit 1 to N, 
         and see which one is visited twice, and which one haven't been visited
    To save space though, we use the original nums[] to mark if we have visited before
         and check which one never been visited
    Think nums[] here as a set of index to visit an array, the value's sign works as a boolean visited/!visited
         Originally if the nums are all correct, we won't see any visited index during visiting
         Originally if the nums are all correct, we won't see any unvisited index after visiting
    */
    public int[] findErrorNums(int[] nums) {
        int[] result = new int[2]; //result[0]: duplicated value, result[1]: missing value;
        
        //Visit an array, with index coming from nums, 
        //if the cell is visited twice, then its index must be duplicated
        for (int i: nums) { //Think nums[] here as a set of index to visit, the value's sign works as a boolean visited/!visited
           if(nums[Math.abs(i) - 1] > 0) {
               //Flip each unvisited number
               nums[Math.abs(i) - 1] *= -1;
           } else {
               //If a number has been visited before, it must be duplicated
               result[0] = Math.abs(i);
           }
        }
        
        //After initial visit, if a number hasn't been visited
        //Then the index to visit such number must be missing
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0) {
                result[1] = i+1;
            }
        }
        return result;
    }
}
```

## [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string/description/)

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
```
Input: 
S = "cba"
T = "abcd"

Output: "cbad"

Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 ```

Note:

* S has length at most 26, and no character is repeated in S.
* T has length at most 200.
* S and T consist of lowercase letters only.

```java
class Solution {
    public String customSortString(String S, String T) {
        //Process S to mark special character
        Set<Character> specials = new HashSet(Arrays.asList(S.toCharArray()));
        for (char c: S.toCharArray()) {
            specials.add(c);
        }
        //Process T to count each character frequency
        Map<Character, Integer> counts = new HashMap<>();
        for (char c: T.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0)+1);
        }
        //Reconstruct a new string based on S's character order
        StringBuilder sb = new StringBuilder();
        for (char c: S.toCharArray()) {
            for (int i = 0; i < counts.getOrDefault(c, 0); i++) {
                sb.append(c);
            }
        }
        for (char c: T.toCharArray()) {
            if (!specials.contains(c))
                sb.append(c);
        }
        return sb.toString();
    }
}
```

## [661. Image Smoother](https://leetcode.com/problems/image-smoother/description/)

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
```
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
 
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
 
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

```java
class Solution {
    private int R;
    private int C;
    
    public int[][] imageSmoother(int[][] M) {
        if (M == null || M.length == 0) return null;
        this.R = M.length;
        this.C = M[0].length;
        int[][] result= new int[M.length][M[0].length];
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                result[i][j] = getAverage(i, j, M);
            }
        }
        return result;
    }
    
    protected int getAverage(int i, int j, int[][] M) {
        float sum = 0; //Total sum of neighbors
        float counts = 0;//Total number of neighbors
        int[][] neighborDiffs = new int[][]{
            {-1,-1},{-1,0},{-1,1},
            {0,-1},{0,0},{0,1}, //Including self in the average
            {1,-1},{1,0},{1,1}
        };
        
        for (int[] diff: neighborDiffs) {
            int x = i+diff[0], y = j+diff[1]; //Neighbor coordinates
            if (inBound(x,y)) {
                counts++;
                sum += M[x][y];
            }
        }
        return (int)Math.floor(sum/counts);
    }
    
    private boolean inBound(int x, int y) {
        return x >= 0 && x < R && y >= 0 && y < C;
    }
}
```

## [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/)

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
```
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

Example 2:
```
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

Example 3:
```
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

Example 4:
```
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

Note: Answer will in the range of 32-bit signed integer.

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

//For each layer
//If    parent          has index of    i
//Then  left child      index is        2*i
//And   right child     index is        2*i + 1
class Solution {
    protected class AnnotatedTreeNode {
        protected int position;
        protected TreeNode node;
        
        AnnotatedTreeNode(int position, TreeNode node) {
            this.position = position;
            this.node = node;
        }
    }

    //The width for each level is defined between the first non-null node to the last non-null node
    //Traversal by level and compute width for each layer
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        int maxWidth = -1;
        
        Queue<AnnotatedTreeNode> queue = new LinkedList<>();
        queue.offer(new AnnotatedTreeNode(0, root));
        
        while(!queue.isEmpty()) {
            int levelNodes = queue.size();
            int first = -1; //The index of first non-null child
            int last = -1; //The index of last non-null child
            
            for (int i = 0; i < levelNodes; i++) {
                AnnotatedTreeNode wrap = queue.poll();
                //Update width marker
                if (first == -1) first = wrap.position;
                last = wrap.position;
                
                //Enqueu non-null nodes
                if (wrap.node.left != null) {
                    queue.offer(new AnnotatedTreeNode(2*wrap.position, wrap.node.left));
                } 
                
                if (wrap.node.right != null) {
                    queue.offer(new AnnotatedTreeNode(2*wrap.position + 1, wrap.node.right));
                }
            }
            if (first == -1) break; //All null node in this level, no need to continue
            maxWidth = Math.max(maxWidth, last - first + 1);
        }
        
        return maxWidth;
    }
}
```

## 663. Equal Tree Partition
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
```
Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
```

Example 2:
```
Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
```

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

//Calculate the sum of each subtree
//Case I: If the total sum is odd, then false
//Case II: If the total sum is 0, make sure at least two subtree have a 0, such as case [0, -1, 1]
//Case III: If exists a subtree whose sum is half of the total sum, then true
class Solution {
    HashMap<TreeNode, Integer> subtreeSum = new HashMap<>();

    public boolean checkEqualTree(TreeNode root) {
        TreeNode node = root;
        buildSubTreeSum(root);
        int totalSum = subtreeSum.get(root);
        
        //Case I
        if (totalSum % 2 != 0) return false;
        
        //Case II
        if (totalSum == 0) {
            int count = 0; //How many subtree has a sum of 0? Must exist a subtree other than root for it to be splittable
            for (Map.Entry<TreeNode, Integer> entry: subtreeSum.entrySet()) {
                if (entry.getValue() == 0) {
                    count++;
                }
            }
            //The subTreeSum at root is 0, there have to be a real subtree whose subTreeSum is 0 to split
            //Think special case [0, -1, 1]
            return count > 1; 
        }
        
        //Case III
        int halfSum = totalSum / 2;
        return subtreeSum.values().contains(halfSum) && halfSum != 0 ;
    }
    
    private int buildSubTreeSum(TreeNode node) {
        if (node == null) {
            return 0;
        } else {
            subtreeSum.put(node, node.val + buildSubTreeSum(node.left) + buildSubTreeSum(node.right));
        }
        return subtreeSum.get(node);
    }
    
}
```

## [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/description/)

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
```
11000
11000
00011
00011

Given the above grid map, return 1.
```

Example 2:
```
11011
10000
00001
11011

Given the above grid map, return 3.
```

Notice that:
```
11
1
```
and
```
 1
11
```
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.

```java
class Solution {
    //Get adjacent neighbor of a given coordinate
    int[][] neighbors={{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    public int numDistinctIslands(int[][] grid) {
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
        return getKey(island);
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

## [396. Rotate Function](https://leetcode.com/problems/rotate-function/description/)

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:
```
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
```

```java
class Solution {
    /*
    Explanation: 
        F(k) =   0 * Bk[0]   + 1 * Bk[1] + ...   + (n-1) * Bk[n-1]
        F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
               =               0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
        Then,

        F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
                      = (Bk[0] + ... + Bk[n-1]) - nBk[0]
                      = sum - nBk[0]
        Thus,
        F(k) = F(k-1) + sum - nBk[0]
        
        ## What is Bk[0]?
        
        ```
        k = 0; B[0] = A[0];
        k = 1; B[0] = A[len-1];
        k = 2; B[0] = A[len-2];
        ...
        ```
    */
    public int maxRotateFunction(int[] A) {
        int allSum = 0;
        int len = A.length;
        int F = 0;
        for (int i = 0; i < len; i++) {
            F+= i*A[i];
            allSum += A[i];
        }
        int max = F;
        for (int i = len - 1; i >= 1; i--) {
            F = F + allSum - len*A[i];  //F(k) = F(k-1) + sum - nBk[0], whereas B[0] = A[len-k]
            max = Math.max(F, max);
        }
        return max;
        
    }
}
```


## [738. Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/description/)

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
```
Input: N = 10
Output: 9
```

Example 2:
```
Input: N = 1234
Output: 1234
```

Example 3:
```
Input: N = 332
Output: 299
```
Note: N is an integer in the range [0, 10^9].

```java
class Solution {
    /*
    The idea is to go from the LSB to MSB and find the last digit, where an inversion happens.
    There are 2 cases to consider:

    case 1:
    In 14267 , we see that inversion happens at 4. In this case, then answer is obtained by reducing 4 to 3, and changing all the following digits to 9.
    => 13999

    case 2:
    1444267, here eventhough the last inversion happens at the last 4 in 1444, if we reduce it to 3, then that itself breaks the rule. So once we find the last digit where inversion happens, if that digit is repeated, then we have to find the last position of that digit. After that it is same as case1, where we reduce it by 1 and set the remaining digits to 9.
    => 1399999

    The steps are:

        1. Convert n into num array in reverse order
        2. Find the leftmost position that is inverted and if the inverted character repeats itself, find the leftmost repeated digit.
        3. Fill the digits after inversion as 9
        4. Reduce the digit that caused the inversion by -1
        5. Reverse back the num array and convert to int
    */
    public int monotoneIncreasingDigits(int N) {
        if (N <= 9) return N;
        
        char[] digits = String.valueOf(N).toCharArray();
        
        int mark = digits.length; //<=== Marker of flipping bit
        for (int i = digits.length - 1; i > 0; i--) { //Step 1: visit in reverse order
            if (digits[i] < digits[i-1]) {
                mark = i-1; //Step 2: Find the leftmost position where the string begin not to increase
                digits[i-1]--; //Step 4: Reduce the digit that caused the inversion by -1
            }
        }
        
        for (int i = mark+1; i < digits.length; i++) {
            digits[i] = '9'; //Step 3: Fill the digits after inversion as 9
        }
        return Integer.parseInt(new String(digits));
    }
}
```
===TODO===
## 646
## 742
## 746
## 762
## 771
## 775
## 776
## 801


