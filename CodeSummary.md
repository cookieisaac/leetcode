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