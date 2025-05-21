class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dp(idx):
            if idx==len(s):
                return -1
            res=inf
            # run from idx and get minimum cuts
            for k in range(idx, len(s)):
                if s[idx:k+1]==s[idx:k+1][::-1]:
                    res=min(res, 1+dp(k+1))
            return res
        return dp(0)
