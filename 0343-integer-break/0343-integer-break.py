class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[1]*(n+1)
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                dp[i]=max(dp[i], (i-j)*dp[j], (i-j)*j)
        return dp[-1]