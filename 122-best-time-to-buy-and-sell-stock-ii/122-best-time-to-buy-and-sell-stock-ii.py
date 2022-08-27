class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit
        
#         dp = {}
        
#         def dfs(index, even):
#             if index == len(prices):
#                 return 0
#             if (index, even) in dp:
#                 return dp[(index, even)]
#             currSum = prices[index] if even else (-1*prices[index])
#             dp[(index, even)] = max(currSum + dfs(index+1, not even), dfs(index+1, even))
#             return dp[(index, even)]
#         return dfs(0, False)