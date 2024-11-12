class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if j+1<len(p) and p[j+1]=='*':
                # you can either include p[j] or not include it
                # removing it
                res1=dp(i,j+2)
                # including it
                res2=False
                if i<len(s) and (s[i]==p[j] or p[j]=='.'):
                    res2=dp(i+1,j)
                return res1 or res2
            if i<len(s) and (s[i]==p[j] or p[j]=='.'):
                return dp(i+1,j+1)
            return False
        return dp(0, 0)