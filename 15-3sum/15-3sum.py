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
            for i in range(l-2):
                left = i+1
                right = l-1
                while left < right:
                    potentialMatch = nums[i] + nums[left] + nums[right]
                    if potentialMatch == 0:
                        ans.append([nums[i] , nums[left] , nums[right]])
                        left += 1
                        right -=1
                    elif potentialMatch < 0:
                        left += 1
                    else:
                        right -=1
            d = {}
            ans1 = []
            for a in ans:
                val = str(a[0])+'_'+str(a[1])+'_'+str(a[2])
                if val not in d:
                    d[val] = True
                    ans1.append(a)
            return ans1