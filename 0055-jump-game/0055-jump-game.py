class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_idx=len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i>=min_idx:
                min_idx=min(min_idx, i)
        return min_idx==0