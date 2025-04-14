class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # treat each ballon as if you can pop it last
        @cache
        def dp(l, r):
            if l>r:
                return 0
            res=-inf
            for i in range(l, r+1):
                res=max(res, dp(l, i-1)+((nums[l-1] if l-1>=0 else 1)*nums[i]*(nums[r+1] if r+1<len(nums) else 1))+dp(i+1, r))
            return res
        return dp(0, len(nums)-1)