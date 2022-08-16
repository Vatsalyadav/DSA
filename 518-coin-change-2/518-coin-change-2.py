class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ways = [0] * (amount+1)
        ways[0] = 1
        
        for coin in coins:
            for index in range(coin,amount+1):
                ways[index] += ways[index-coin]
        return ways[-1]