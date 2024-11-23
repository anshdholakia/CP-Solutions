class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # use a sliding window
        res=0
        l=0
        cur_m=1
        for r in range(len(nums)):
            cur_m*=nums[r]
            while l<=r and cur_m>=k:
                cur_m/=nums[l]
                l+=1
            res+=(r-l+1)
        return res