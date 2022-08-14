class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        
        ans = []
        index = 0
        minDiff = abs(arr[0] - arr[1])
        while index < len(arr) - 1:
            currDiff = abs(arr[index] - arr[index+1])
            if currDiff == minDiff:
                ans.append([arr[index] , arr[index+1]])
            elif currDiff < minDiff:
                minDiff = currDiff
                ans = [[arr[index] , arr[index+1]]]
            index+=1
        return ans
            