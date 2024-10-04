class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        SUM = sum(nums)
        if SUM%k:
            return False
        EACH_SUM = SUM//k
        nums.sort()
        used = [False]*len(nums)
        def backtrack(cur_k, x, cur_sum):
            if cur_k==k:
                return True
            if cur_sum==EACH_SUM:
                return backtrack(cur_k+1, 0, 0)
            for j in range(x, len(nums)):
                if used[j] or cur_sum+nums[j]>EACH_SUM:
                    continue
                if j > x and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue
                used[j] = True
                if backtrack(cur_k, j+1, cur_sum+nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, 0, 0)
        