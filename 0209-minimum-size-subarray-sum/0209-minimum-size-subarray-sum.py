class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        cur=0
        res=inf
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>=target:
                res=min(res, r-l+1)
                cur-=nums[l]
                l+=1
        return 0 if res==inf else res