class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get as much profit as you can
        profit=0
        l=0
        for r in range(1, len(prices)):
            if prices[r]>prices[l]:
                profit+=prices[r]-prices[l]
            l=r
        return profit