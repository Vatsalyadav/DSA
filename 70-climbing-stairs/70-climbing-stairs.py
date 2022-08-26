class Solution(object):
    def climbStairs(self, n, memo = {}):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 1
        elif n < 0:
            return 0
        if n-1 not in memo:
            memo[n-1] = self.climbStairs(n-1, memo)
        if n-2 not in memo:
            memo[n-2] = self.climbStairs(n-2, memo)
        return memo[n-1] + memo[n-2]
        