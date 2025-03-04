class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, buying):
            if i>=len(prices):
                return 0
            if buying:
                buy=-prices[i]+dfs(i+1, not buying)
                cooldown=dfs(i+1, buying)
                return max(buy, cooldown)
            else:
                sell=prices[i]+dfs(i+2, not buying)
                cooldown=dfs(i+1, buying)
                return max(sell, cooldown)
        return max(0, dfs(0, True))