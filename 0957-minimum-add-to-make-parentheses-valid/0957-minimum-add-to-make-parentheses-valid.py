class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for c in s:
            if c==')':
                if not stack or stack[-1]==')':
                    stack.append(c)
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack)