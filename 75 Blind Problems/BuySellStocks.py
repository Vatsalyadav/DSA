# LeetCode Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfitBruteForce(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time = O(n^2)
        if len(prices) < 2:
            return 0

        maxDiff = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > maxDiff:
                    maxDiff = prices[j] - prices[i]
        return maxDiff

    def maxProfitSlidingWindow(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time = O(n)
        b = prices[0]
        s = prices[0]
        maxProfit = 0
        i = 0
        while i < len(prices):
            if prices[i] < b:
                b = prices[i]
                s = prices[i]
            elif prices[i] > s:
                s = prices[i]
            if s - b > maxProfit:
                maxProfit = s - b
            i += 1
        return maxProfit


solutionObj = Solution()
print(solutionObj.maxProfitBruteForce([7,1,5,3,6,4]))