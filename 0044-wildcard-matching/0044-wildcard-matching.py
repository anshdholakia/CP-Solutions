class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p) or (i>=len(s) and p[j]!='*'):
                return False
            if p[j]=='*':
                # keep j on * or move
                return (dp(i+1, j) if i<len(s) else False) or dp(i+1, j+1) or dp(i, j+1)
            if p[j]=='?':
                return dp(i+1, j+1)
            return s[i]==p[j] and dp(i+1, j+1)
        return dp(0, 0)