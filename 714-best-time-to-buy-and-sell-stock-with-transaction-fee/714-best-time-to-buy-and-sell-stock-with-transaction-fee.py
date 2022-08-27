class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = {}
        
        def dfs(index, even):
            if index == len(prices):
                return 0
            if (index, even) in dp:
                return dp[(index, even)]
            currSum = prices[index] if even else (-1*prices[index])
            dp[(index, even)] = max(currSum + dfs(index+1, not even) - (fee/2.0), dfs(index+1, even))
            return dp[(index, even)]
        return int(dfs(0, False))