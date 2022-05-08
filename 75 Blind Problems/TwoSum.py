# LeetCode link: https://leetcode.com/problems/two-sum/submissions/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        count = 0
        for n in nums:
            potentialNum = target - n
            if potentialNum in numDict:
                return [numDict[potentialNum], count]
            else:
                numDict[n] = count
            count += 1
        return []


solutionObj = Solution()
print(solutionObj.twoSum([2, 7, 11, 15], 9))

