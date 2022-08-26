class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        def dfs(index, even):
            if index >= len(nums):
                return 0
            if (index, even) in dp:
                return dp[(index, even)]
            val = nums[index] if even else (-1 * nums[index])
            dp[(index, even)] = max(val + dfs(index+1, not even), dfs(index+1, even))
            return dp[(index, even)]
        
        return dfs(0, True)