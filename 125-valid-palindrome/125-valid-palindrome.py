class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s)).lower()
        # return new == new[::-1]
        left = 0
        right = len(new)-1
        while left<right:
            if new[left] != new[right]:
                return False
            else:
                left+=1
                right-=1
        return True