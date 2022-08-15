class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1

        a,b = 1,2
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b