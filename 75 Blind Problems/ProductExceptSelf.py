# LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Method: right and left product sliding window
        # Time: O(n)
        result = [1] * len(nums)
        pl = 1
        pr = 1

        for i in range(1, len(nums)):
            pl *= nums[i - 1]
            result[i] *= pl

        for i in range(len(nums) - 2, -1, -1):
            pr *= nums[i + 1]
            result[i] *= pr

        return result