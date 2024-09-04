class Solution:
    def jump(self, nums: List[int]) -> int:
        for i in range(1, len(nums)-1):
            nums[i] = max(nums[i]+i, nums[i-1])
        result=0
        pos=0
        while pos<len(nums)-1:
            pos=nums[pos]
            result+=1
        return result
