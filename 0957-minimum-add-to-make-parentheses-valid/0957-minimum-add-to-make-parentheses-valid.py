class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
            if c=='(':
                stack.append(c)
            elif stack and stack[-1]=='(':
                    stack.pop()
            else:
                stack.append(c)
        return len(stack)
        