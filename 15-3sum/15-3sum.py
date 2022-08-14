class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        l = len(nums)
        if len(set(nums))== 1 and set(nums) == set([0]):
            return [[0,0,0]]
        
        else:
            nums.sort()
            ans = []
            d = {}
            for i in range(l-2):
                left = i+1
                right = l-1
                while left < right:
                    potentialMatch = nums[i] + nums[left] + nums[right]
                    if potentialMatch == 0:
                        sortedMatch = sorted([nums[i], nums[left], nums[right]])
                        potentialMatchStr = str(sortedMatch[0])+'_'+str(sortedMatch[1])+'_'+str(sortedMatch[2])
                        if potentialMatchStr not in d:
                            ans.append([nums[i] , nums[left] , nums[right]])
                            d[potentialMatchStr] = True
                        left += 1
                        right -=1
                    elif potentialMatch < 0:
                        left += 1
                    else:
                        right -=1
            return ans