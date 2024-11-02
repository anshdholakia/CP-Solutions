class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        res=0
        for i, c in enumerate(s):
            if c==')':
                if not stack:
                    stack.append((')',i))
                elif stack[-1][0]=='(':
                    stack.pop()
                    if not stack:
                        res=max(res, i+1)
                    else:
                        res=max(res, i-stack[-1][1])
                else:
                    stack.pop()
                    stack.append((')', i))
            else:
                stack.append(('(', i))
        return res