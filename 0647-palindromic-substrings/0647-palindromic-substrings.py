class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count+= self.oddLenPalindromes(i, s) + self.evenLenPalindromes(i, s)
        return count
    
    def oddLenPalindromes(self, i, s):
        left = i
        right = i
        count = 0
        while left>=0 and right<len(s):
            if s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            else:
                break
        return count
    
    def evenLenPalindromes(self, i, s):
        left = i
        right = i+1
        count = 0
        while left>=0 and right<len(s):
            if s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            else:
                break
        return count