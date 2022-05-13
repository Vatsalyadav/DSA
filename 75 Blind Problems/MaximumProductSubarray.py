# Leetcode Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        mm = [1,1]
        res = max(nums)
        for n in nums:
            if n==0:
                mm[0] =1
                mm[1] =1
                continue
            else:
                temp=mm[0]*n
                mm[0] =max(mm[0]*n,mm[1]*n,n)
                mm[1] =min(temp,mm[1]*n,n)
                res = max(res,mm[0])
        return res
