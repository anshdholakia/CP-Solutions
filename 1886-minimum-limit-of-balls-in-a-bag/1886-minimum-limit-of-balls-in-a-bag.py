class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        res=r
        def check(k):
            ops=0
            for n in nums:
                if n<=k:
                    continue
                ops+=ceil((n-k)/k)
            return ops<=maxOperations
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res