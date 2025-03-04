class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums=set({0})
        for s in stones:
            for l in sums.copy():
                sums.add(s+l)
        res=inf
        SUM=sum(stones)
        for s in sums:
            res=min(res, abs((SUM-s)-s))
        return res
