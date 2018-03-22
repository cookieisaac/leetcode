Ordered by frequency as of March 21, 2018

## 739 Partition Labels
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

## 1. Two Sum

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

## 3. Valid Parenthese

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

## 200 Number of Islands

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

## 675 Cut Off Trees for Golf Event

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
        for (int i = 1; i < parsed.length;) {
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