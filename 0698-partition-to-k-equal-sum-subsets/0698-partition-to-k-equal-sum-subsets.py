class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target=sum(nums)
        if target%k:return False
        target//=k
        used=[False]*len(nums)
        nums.sort(reverse=True)
        def backtrack(i, k, cur_sum):
            if k==0:
                return True
            if cur_sum==target:
                return backtrack(0, k-1, 0)
            for j in range(i, len(nums)):
                if j>0 and not used[j-1] and nums[j]==nums[j - 1]:
                    continue
                if not used[j] and cur_sum+nums[j]<=target:
                    used[j]=True
                    if backtrack(j+1, k, cur_sum+nums[j]):
                        return True
                    used[j]=False
            return False
        return backtrack(0, k, 0)