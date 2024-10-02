class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        def backtrack(cur_nums, prev):
            nonlocal result
            if not cur_nums:
                result+=1
                return
            for k in range(len(cur_nums)):
                if (k+1<len(cur_nums) and cur_nums[k+1]==cur_nums[k]) or (prev!=None and prev+cur_nums[k]!=math.isqrt(prev+cur_nums[k])**2):
                    continue
                backtrack(cur_nums[:k]+cur_nums[k+1:], cur_nums[k])
        backtrack(nums, None)
        return result