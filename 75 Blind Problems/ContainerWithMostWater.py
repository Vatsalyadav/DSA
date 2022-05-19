# LeetCode Link: https://leetcode.com/problems/container-with-most-water/submissions/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Method: Two pointer
        # Time: O(n)
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            store = (right - left) * min(height[left], height[right])
            if res < store:
                res = store
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res