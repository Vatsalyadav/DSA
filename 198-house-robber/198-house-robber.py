class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        if l < 3:
            return max(nums)
        
        if l == 3:
            return max(nums[1], nums[0]+nums[2])
        
#         grid = [maxSumButAdjacentToNext, maxSumButNotAdjacentToNext, maxButNotAdj, maxButAdj ]
        grid = [max(nums[1], nums[0]+nums[2]), nums[1], max(nums[:2]), max(nums[:3])]
        index = 3
        while index < len(nums):
            grid = [nums[index] + max(grid[1], grid[2]), max(grid), max(grid[2], grid[3]), max(nums[index], grid[2], grid[3])]
            index+=1
            print(grid)
        return max(grid)
            