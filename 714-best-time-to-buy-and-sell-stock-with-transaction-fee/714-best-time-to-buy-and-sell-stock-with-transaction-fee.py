class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i] )
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)

        return sell[-1]
#         dp = {}
        
#         def dfs(index, even):
#             if index == len(prices):
#                 return 0
#             if (index, even) in dp:
#                 return dp[(index, even)]
#             currSum = prices[index] if even else (-1*prices[index])
#             dp[(index, even)] = max(currSum + dfs(index+1, not even) - (fee/2.0), dfs(index+1, even))
#             return dp[(index, even)]
#         return int(dfs(0, False))