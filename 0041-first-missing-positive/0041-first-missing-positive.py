class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # replace the negatives with len(nums)+1
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=len(nums)+1
        for i in range(len(nums)):
            if abs(nums[i])<=len(nums) and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*=-1
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)+1