class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            curr = num
            digits = 0
            while curr>0:
                curr/=10
                digits+=1
            if digits%2==0:
                count+=1
        return count