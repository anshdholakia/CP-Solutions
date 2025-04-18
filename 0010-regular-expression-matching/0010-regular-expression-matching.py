class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if j>=len(p):
                return i>=len(s)
            if j+1<len(p) and p[j+1]=='*':
                # either take * or skip it
                # skip
                res1=dp(i, j+2)
                # take
                res2=False
                if i<len(s) and (s[i]==p[j] or p[j]=='.'):
                    res2=dp(i+1, j)
                return res1 or res2
            elif i<len(s) and (s[i]==p[j] or p[j]=='.'):
                return dp(i+1, j+1)
            return False
        return dp(0, 0)