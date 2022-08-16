class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seq = []
        
        for num in nums:
            pos = -1
            for i in range(len(seq)):
                if num <= seq[i]:
                    pos = i
                    break
            if pos == -1:
                seq.append(num)
            else:
                seq[pos] = num
        return len(seq)
            