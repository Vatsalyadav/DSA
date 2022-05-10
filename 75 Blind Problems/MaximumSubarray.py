class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: Contracting overall window by removing lower contributor (Test cases 181/209 successful)
        # Time: O(n)
        maxSum = sum(nums)
        left = 0
        right = len(nums) - 1
        currSum = maxSum
        while left < right:
            print(currSum, nums[left:right + 1])
            if nums[left] < nums[right]:
                currSum -= nums[left]
                left += 1
            else:
                currSum -= nums[right]
                right -= 1
            maxSum = max(currSum, maxSum)
        return maxSum

    def maxSubArray(self, nums):
        # Method 2: Calculate currentSum and add new number
        # if new number is greater than the total sum so far, reassign currSum and continue. Keep taking maxSum so far
        # Time: O(n)
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            if currSum + nums[i] < nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum

    def maxSubArray(self, nums):
        # Method 3: Sums is max possible sum at each index by contribution of numbers till that index
        # Time: O(n)
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = max(nums[i], sums[i] + sums[i - 1] + nums[i])
        return max(sums)