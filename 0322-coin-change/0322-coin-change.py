class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[inf]*(amount+1)
        dp[0]=0
        for amt in range(0, len(dp)):
            for c in coins:
                if amt-c>=0:
                    dp[amt]=min(dp[amt], dp[amt-c]+1)
        return dp[-1] if dp[-1]!=inf else -1