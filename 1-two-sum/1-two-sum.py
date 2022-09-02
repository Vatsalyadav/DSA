class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for index, num in enumerate(nums):
            potentialMatch = target - num
            
            if potentialMatch in d:
                return [d[potentialMatch], index]
            else:
                d[num] = index
            