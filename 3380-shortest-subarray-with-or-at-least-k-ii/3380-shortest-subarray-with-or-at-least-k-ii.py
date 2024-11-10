class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k==0:
            return 1
        # xor helps you return back
        curres=0
        bits=[0]*32 # 32-bit system
        l=0
        res=inf
        for r in range(len(nums)):
            curn=nums[r]
            for i in range(32):
                if curn&1:
                    bits[i]+=1
                curn>>=1
            curres|=nums[r]
            while curres>=k:
                res=min(res, r-l+1)
                # correct curres
                curn=nums[l]
                for i in range(32):
                    if curn&1:
                        bits[i]-=1
                    curn>>=1
                curres=0
                for i, b in enumerate(bits):
                    if b>0:
                        curres|=2**i
                l+=1
        return res if res!=inf else -1