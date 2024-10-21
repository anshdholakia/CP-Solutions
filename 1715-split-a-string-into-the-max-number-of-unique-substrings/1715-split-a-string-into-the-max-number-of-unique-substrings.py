class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited=set({})
        result = 0
        def backtrack(cur_s):
            nonlocal result
            if len(visited)>result:
                result=len(visited)
            for i in range(len(cur_s)):
                if cur_s[:i+1] not in visited:
                    visited.add(cur_s[:i+1])
                    backtrack(cur_s[i+1:])
                    visited.remove(cur_s[:i+1])
        backtrack(s)
        return result