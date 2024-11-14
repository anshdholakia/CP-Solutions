class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=True
        minimum=len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i>=minimum:
                minimum=i
                res=True
            else:
                res=False
        return res