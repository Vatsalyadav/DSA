# LeetCode Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfitBruteForce(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        maxDiff = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > maxDiff:
                    maxDiff = prices[j] - prices[i]
        return maxDiff

solutionObj = Solution()
print(solutionObj.maxProfitBruteForce([7,1,5,3,6,4]))