class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        res=0
        idx=0
        while idx<len(s):
            if s[idx]==')':
                if stack and stack[-1][0]=='(':
                    _, i = stack.pop()
                    if stack:
                        res=max(res, idx-stack[-1][1])
                    else:
                        res=max(res, idx+1)
                else:
                    stack.append((')', idx))
            else:
                stack.append(('(', idx))
            idx+=1
        return res