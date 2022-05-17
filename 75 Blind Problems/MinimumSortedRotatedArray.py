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

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Method: Use binary search to find pivot
        # Use Binary search to find number using pivot
        # Time: O(logn)
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        start = left
        left = 0
        right = len(nums) - 1

        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start

        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
