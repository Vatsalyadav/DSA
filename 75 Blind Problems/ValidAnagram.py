# LeetCode Link: https://leetcode.com/problems/valid-anagram/submissions/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        d = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        for ch in t:
            if ch not in d or d[ch] == 0:
                return False
            else:
                d[ch] -= 1

        return True