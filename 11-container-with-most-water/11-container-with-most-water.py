class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        left, right = 0, len(height)-1
        
        while left < right:
            maxWater = max(maxWater, min(height[left], height[right])*(right-left))
            if height[right] >= height[left]:
                left+=1
            else:
                right-=1
           
        return maxWater