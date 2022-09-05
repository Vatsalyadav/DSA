class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        stack = []
        for ch in s:
            if ch == ']':
                i = len(stack) - 1
                while i > 0:
                    if stack[i] == '[':
                        curr = stack[i+1:len(stack)]
                        if i-3 >= 0 and "".join(stack[i-3:i]).isnumeric():
                            curr *= int("".join(stack[i-3:i]))
                            stack = stack[:i-3] + curr
                        elif i-2 >= 0 and "".join(stack[i-2:i]).isnumeric():
                            curr *= int("".join(stack[i-2:i]))
                            stack = stack[:i-2] + curr
                        else:
                            curr *= int(stack[i-1])
                            stack = stack[:i-1] + curr
                        break
                    else:
                        i-=1
            else:
                stack.append(ch)
        return "".join(stack)