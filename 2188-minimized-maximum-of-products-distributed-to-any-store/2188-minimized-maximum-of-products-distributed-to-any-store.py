class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search to find the result
        l, r= 1, max(quantities)
        def check(single):
            required=0
            for q in quantities:
                required+=ceil(q/single)
            return required<=n
        res=inf
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res