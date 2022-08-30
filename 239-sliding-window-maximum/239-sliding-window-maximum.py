class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
#         Monotonically decreasing queue
#         We are using queue because we want to push a new element 
#         and pop an element from the end when the window moves in O(1) constant time    
        
        output = []
#         queue will hold the indexes of the numbers in decreasing order for a given window
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
#             while q is not empty and the top value is less than the value we are inserting, we will pop the smaller value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
#             if left value is out of bound, remove the left value
            if l > q[0]:
                q.popleft()
            
#             since we are starting at left and right 0, we need to make sure that our window is at least size k
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
            
        return output
            
            
        
        
#         Brute Force
#         ans = [0] * (len(nums) - k +1)
#         l = 0
#         r = k - 1
#         while r < len(nums):
#             ans[l] = max(nums[l:r+1])
#             l+=1
#             r+=1
#         return ans
        