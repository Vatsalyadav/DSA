class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        ans = [float("inf")] * (amount+1)
        ans[0] = 0
        for coin in coins:
            for index in range(coin, amount+1):
                ans[index] = min(ans[index], 1 + ans[index - coin])
        return ans[-1] if ans[-1]!=float("inf") else -1