class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            cur_h=0
            for p in piles:
                cur_h+=ceil(p/mid)
            return cur_h<=h
        l, r = 1, max(piles)
        res=max(piles)
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res