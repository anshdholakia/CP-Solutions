class Solution:
    def numSquares(self, n: int) -> int:
        dp=[inf]*(n+1)
        dp[0]=0
        for amt in range(1, len(dp)):
            for k in range(1, int(sqrt(amt))+1):
                    dp[amt]=min(dp[amt-k**2]+1, dp[amt])
        return dp[-1]