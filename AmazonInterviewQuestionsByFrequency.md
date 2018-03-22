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
