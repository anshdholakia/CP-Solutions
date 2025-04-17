class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorthms
        res=-inf
        curs=0
        for n in nums:
            curs+=n
            res=max(res, curs)
            if curs<0:
                curs=0
        return res