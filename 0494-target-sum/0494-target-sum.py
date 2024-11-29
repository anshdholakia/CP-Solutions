class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def backtrack(x, cur_t):
            if x==len(nums):
                return cur_t==target
            return backtrack(x+1, cur_t-nums[x]) + backtrack(x+1, cur_t+nums[x])
        return backtrack(0, 0)