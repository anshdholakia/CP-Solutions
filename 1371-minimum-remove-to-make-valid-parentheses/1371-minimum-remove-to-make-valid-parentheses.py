class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # store the idx of the bracket in stack
        stack=[]
        for i, c in enumerate(s):
            if c==')':
                if not stack or stack[-1][0]==')':
                    stack.append((c, i))
                elif stack[-1][0]=='(':
                    stack.pop()
            elif c=='(':
                stack.append((c, i))
        removed=0
        for _, idx in stack:
            s=s[:(idx-removed)]+s[(idx-removed)+1:]
            removed+=1
        return s