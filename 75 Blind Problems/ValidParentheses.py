# LeetCode Link: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Method: Stack problem
        # Time: O(n)
        bracketPairs = {")":"(","}":"{","]":"["}
        res = []
        for i in range(len(s)):
            if len(res)==0:
                res.append(s[i])
            elif s[i] in bracketPairs and res[-1] == bracketPairs[s[i]]:
                res.pop()
            else:
                res.append(s[i])

        return True if len(res)==0 else False