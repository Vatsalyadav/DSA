class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = nums[0]
        maxEndingHere = nums[0]
        for num in nums[1:]:
            maxEndingHere = max(maxEndingHere + num, num)
            ans = max(ans, maxEndingHere)
        return ans