class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        res=0
        def check(mid):
            cur_k=0
            for amt in candies:
                cur_k+=(amt//mid)
            return cur_k>=k
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                l=m+1
            else:
                r=m-1
        return res