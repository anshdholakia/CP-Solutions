class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # split this into piles close to the mid way of the stones
        SUM=sum(stones)
        HALF=SUM//2
        sums=set({0})
        res=inf
        for s in stones:
            for curs in sums.copy():
                curs+=s
                HALF1=SUM-curs
                res=min(res, abs(HALF1-curs))
                sums.add(curs)
        return res