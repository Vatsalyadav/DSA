class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        grid = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1+ grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
    
#     Recursive approach with dp grid
#         return self.longestCommonSubsequenceHelper(text1, text2, 0, 0, grid)
        
    
#     def longestCommonSubsequenceHelper(self, text1, text2, i, j, grid):
#         if i >= len(text1) or j >= len(text2):
#             return 0
#         if text1[i] == text2[j]:
#             grid[i][j] = 1 + self.longestCommonSubsequenceHelper(text1, text2, i+1, j+1, grid)
#         else:
#             grid[i][j] = max(self.longestCommonSubsequenceHelper(text1, text2, i, j+1, grid), self.longestCommonSubsequenceHelper(text1, text2, i+1, j, grid))
#         return grid[i][j]
    
            
#        Recursive approach with substrings
#         if len(text1) == 0 or len(text2) == 0:
#             return 0
#         if text1[0] == text2[0]:
#             return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
#         else:
#             return max(self.longestCommonSubsequence(text1, text2[1:]), self.longestCommonSubsequence(text1[1:], text2))

