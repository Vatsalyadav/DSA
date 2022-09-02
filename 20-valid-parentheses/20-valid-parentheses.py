class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','[':']','{':'}'}
        stack = [s[0]]
        for index in range(1, len(s)):
            if stack and stack[-1] in brackets and brackets[stack[-1]] == s[index]:
                stack.pop()
            else:
                stack.append(s[index])
        return len(stack)==0