class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(l, r):
            if l>r:
                return 0
            res=0
            for k in range(l, r+1):
                cur=(nums[l-1] if l>0 else 1)*nums[k]*(nums[r+1] if r+1<len(nums) else 1)
                res=max(res, dp(l,k-1)+cur+dp(k+1, r))
            return res
        return dp(0, len(nums)-1)