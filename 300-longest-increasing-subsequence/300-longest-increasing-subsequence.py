class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], memo[j]+1)
        return max(memo)
# #       Unique Approach: Patience Sort
#         seq = []
        
#         for num in nums:
#             pos = -1
#             for i in range(len(seq)):
# #                 find left most number that is greater than new number, use binary search here
#                 if num <= seq[i]:
#                     pos = i
#                     break
#             if pos == -1:
#                 seq.append(num)
#             else:
#                 seq[pos] = num
#         return len(seq)