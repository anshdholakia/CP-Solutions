class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # replace negative with out of bounds
        bounds=len(nums)
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=bounds+1
        for i in range(len(nums)):
            if abs(nums[i])-1<len(nums) and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*=-1
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return bounds+1
