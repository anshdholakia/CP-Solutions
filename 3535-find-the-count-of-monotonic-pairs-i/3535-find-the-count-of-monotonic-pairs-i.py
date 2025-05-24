class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        @cache
        def dp(idx, i, j):
            if idx==len(nums):
                return 1
            res=0
            for k in range(nums[idx]+1):
                one, two = k, nums[idx]-k
                if (i==None or i<=one) and (j==None or j>=two):
                    res+=dp(idx+1, one, two)
            return res
        return dp(0, None, None)%(10**9+7)