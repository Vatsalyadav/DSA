class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            
            while l <= r:
                if (ord(s[l]) >= 48 and ord(s[l]) <= 57) or (ord(s[l]) >= 97 and ord(s[l]) <= 122) or (ord(s[l]) >= 65 and ord(s[l]) <= 90):
                    break
                else:
                    l+=1
        
            while l <= r:
                if (ord(s[r]) >= 48 and ord(s[r]) <= 57) or (ord(s[r]) >= 97 and ord(s[r]) <= 122) or (ord(s[r]) >= 65 and ord(s[r]) <= 90):
                    break
                else:
                    r-=1
            
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True