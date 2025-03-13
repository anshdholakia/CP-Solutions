class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ps={0:-1}
        SUM=sum(nums)
        if SUM%p==0:
            return 0
        CUR=0
        REM=SUM%p
        size=len(nums)
        for i, n in enumerate(nums):
            CUR+=n
            CUR_MOD=CUR%p
            x=(CUR_MOD-REM)%p
            # find x in ps
            if x in ps:
                size=min(size, i-ps[x])
            ps[CUR_MOD]=i
        return size if size!=len(nums) else -1