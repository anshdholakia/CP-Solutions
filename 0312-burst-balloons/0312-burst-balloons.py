class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(left, right):
            if left>right:
                return 0
            res=-inf
            for i in range(left, right+1):
                # select i to be popped last
                res=max(res, dp(left, i-1)+dp(i+1, right)+nums[i]*(nums[right+1] if right+1<len(nums) else 1)*(nums[left-1] if left>0 else 1))
            return res

        return dp(0, len(nums)-1)