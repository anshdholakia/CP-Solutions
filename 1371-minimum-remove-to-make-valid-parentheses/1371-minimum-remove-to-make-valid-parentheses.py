class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_keep = set({})
        for i in range(len(s)):
            if s[i]=='(':
                # append to the stack with the current i and index of opening bracket
                stack.append(i)
            elif s[i]==')':
                if stack:
                    to_keep.add(stack.pop())
                    to_keep.add(i)
        result = ""
        for i in range(len(s)):
            if s[i] in '()' and i not in to_keep:
                continue
            result+=s[i]
        return result