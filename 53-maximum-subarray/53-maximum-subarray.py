class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = float("-inf")
        maxEndingHere = float("-inf")
        for num in nums:
            maxEndingHere = max(maxEndingHere + num, num)
            ans = max(ans, maxEndingHere)
        return ans