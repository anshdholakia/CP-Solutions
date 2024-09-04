class Solution:
    def canJump(self, nums: List[int]) -> bool:
        minimum = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i>=minimum:
                minimum=i
        return minimum==0
