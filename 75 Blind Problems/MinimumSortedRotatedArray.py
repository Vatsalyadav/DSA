# Leetcode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method: Modified binary search
        # Time: O(log n)
        right = len(nums) - 1
        left = 0
        mid = right // 2

        while mid < right and mid > left:
            leftNum = nums[left]
            rightNum = nums[right]
            midNum = nums[mid]

            if leftNum < midNum and leftNum > rightNum:
                left = mid
            if rightNum > midNum:
                right = mid
            mid = (left + right) // 2
        return min(nums[right], nums[left])