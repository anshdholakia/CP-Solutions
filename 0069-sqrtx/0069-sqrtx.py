class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0
        l, r = 1, x
        res=l
        while l<=r:
            m=(l+r)//2
            if m**2<=x:
                res=m
                l=m+1
            else:
                r=m-1
        return res