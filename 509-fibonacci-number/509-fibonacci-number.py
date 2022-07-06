class Solution(object):
    def fib(self, n, memo = {}):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
        
            if n-1 not in memo:
                memo[n-1] = self.fib(n-1, memo)
            if n-2 not in memo:
                memo[n-2] = self.fib(n-2, memo)
            
            return memo[n-2] + memo[n-1]
        