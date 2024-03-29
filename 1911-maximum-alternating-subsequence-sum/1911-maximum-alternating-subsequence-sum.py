class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumOdd = sumEven = 0
        for i in range(len(nums)-1, -1, -1):
            tempEven = max(sumOdd + nums[i], sumEven)
            tempOdd = max(sumEven - nums[i], sumOdd)
            sumOdd, sumEven = tempOdd, tempEven
        return sumEven
            
    
#     Decision Tree Approach
#         dp = {}
#         def dfs(index, even):
#             if index >= len(nums):
#                 return 0
#             if (index, even) in dp:
#                 return dp[(index, even)]
#             val = nums[index] if even else (-1 * nums[index])
#             dp[(index, even)] = max(val + dfs(index+1, not even), dfs(index+1, even))
#             return dp[(index, even)]
        
#         return dfs(0, True)