class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cur_s = []
        removed = 0
        for i in range(len(s)):
            if s[i]==')':
                if not stack:
                    removed+=1
                    continue
                else:
                    stack.pop()
            elif s[i]=='(':
                stack.append(i-removed)
            cur_s.append(s[i])
        removed = 0
        for i in stack:
            cur_s.pop(i-removed)
            removed+=1
        return "".join(cur_s)
