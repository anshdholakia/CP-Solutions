class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp=[[0]*(len(coins)+1) for _ in range(amount+1)]
        dp[0]=[1]*(len(coins)+1)
        for amt in range(1, len(dp)):
            for i, c in enumerate(coins):
                if amt-c>=0:
                    dp[amt][i+1]=(dp[amt-c][i+1]+dp[amt][i])
                else:
                    dp[amt][i+1]=dp[amt][i]
        return dp[-1][-1]
        