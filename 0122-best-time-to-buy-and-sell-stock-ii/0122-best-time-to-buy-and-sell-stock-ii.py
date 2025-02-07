class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        l=0
        for r in range(1, len(prices)):
            if prices[r]>prices[l]:
                total+=prices[r]-prices[l]
                l=r
            else:
                l=r
        return total