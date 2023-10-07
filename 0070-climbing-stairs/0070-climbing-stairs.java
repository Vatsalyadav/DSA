class Solution {
    public int climbStairs(int n) {
        return climbStairsHelper(n, new HashMap<Integer, Integer>());
    }
    
    public int climbStairsHelper(int n, HashMap<Integer, Integer> memo) {
        if(n == 0)
            return 1;
        else if(n<0)
            return 0;
        
        if(!memo.containsKey(n-1))
            memo.put(n-1, climbStairsHelper(n-1, memo));
        if(!memo.containsKey(n-2))
            memo.put(n-2, climbStairsHelper(n-2, memo));
        return memo.get(n-1) + memo.get(n-2);
    }
}