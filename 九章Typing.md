## Subsets

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> solutions = new ArrayList<>();
        backtrack(nums, solutions, new ArrayList<>(), 0);
        return solutions;
    }
    
    private void backtrack(int[] nums, List<List<Integer>> solutions, List<Integer> solution, int start) {
        solutions.add(new ArrayList<>(solution));
        
        for (int i = start; i < nums.length; i++) {
            solution.add(nums[i]);
            backtrack(nums, solutions, solution, i+1);
            solution.remove(solution.size() - 1);
        }
    }
}
```

## Subsets II
```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, result, new ArrayList<>(), 0);
        return result;
    }
    
    private void backtrack(int[] nums,  List<List<Integer>> result, List<Integer> subset, int start) {
        result.add(new ArrayList<>(subset));
        
        for (int i = start; i < nums.length; i++) {
            if ( i > start && nums[i] == nums[i-1]) {
                continue;
            }
            subset.add(nums[i]);
            backtrack(nums, result, subset, i+1);
            subset.remove(subset.size() - 1);
        }
    }
}
```

## Permute
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, nums, new ArrayList<>(), new boolean[nums.length]);
        return result;
    }
    
    public void backtrack(List<List<Integer>> result, int[] nums, List<Integer> prefix, boolean[] visited) {
        if (prefix.size() == nums.length) {
            result.add(new ArrayList<>(prefix));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            prefix.add(nums[i]); visited[i] = true;
            backtrack(result, nums, prefix, visited);
            prefix.remove(prefix.size() - 1); visited[i] = false;
        }
    }
}
```

## Permute II
```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(result, nums, new ArrayList<>(), new boolean[nums.length]);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, int[] nums, List<Integer> prefix, boolean[] visited) {
        if (prefix.size() == nums.length) {
            result.add(new ArrayList<>(prefix));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            if (i > 0 && nums[i] == nums[i-1]  && visited[i-1]) {
                continue;
            }
            prefix.add(nums[i]); visited[i] = true;
            backtrack(result, nums, prefix, visited);
            prefix.remove(prefix.size() - 1); visited[i] = false;
        }
    }
}
```

