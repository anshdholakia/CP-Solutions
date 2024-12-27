class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp=values[0]
        res=-inf
        for i in range(1, len(values)):
            res=max(res, dp+values[i]-i)
            dp=max(dp, values[i]+i)
        return res