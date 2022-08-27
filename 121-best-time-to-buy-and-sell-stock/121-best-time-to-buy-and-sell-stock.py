class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        l = r = 0
        ans = 0 
        while r < len(prices):
            ans = max(ans, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r+=1
        return ans