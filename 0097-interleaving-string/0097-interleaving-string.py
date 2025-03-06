class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=(len(s1)+len(s2)):
            return False
        @cache
        def dp(i, j):
            if i==len(s1) and j==len(s2):
                return True
            if i<len(s1) and j<len(s2) and s1[i]==s3[i+j] and s2[j]==s3[i+j]:
                return dp(i+1, j) or dp(i, j+1)
            elif i<len(s1) and s1[i]==s3[i+j]:
                return dp(i+1, j)
            elif j<len(s2) and s2[j]==s3[i+j]:
                return dp(i, j+1)
            return False
        return dp(0, 0)
