class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, num in enumerate(nums):
            if (target - num) in d:
                return [index, d[target - num]]
            else:
                d[num] = index
        return False