class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swap all 0s and 2s
        l, r = 0, len(nums)-1
        while l<r:
            if nums[r]==0 and nums[l]==2:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[r]!=0:
                r-=1
            if nums[l]!=2:
                l+=1
        # swap all 0s and 1s
        l, r = 0, len(nums)-1
        while l<r:
            if nums[r]==0 and nums[l]==1:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[r]!=0:
                r-=1
            if nums[l]!=1:
                l+=1
        # swap all 2s and 1s
        l, r = 0, len(nums)-1
        while l<r:
            if nums[r]==1 and nums[l]==2:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[r]!=1:
                r-=1
            if nums[l]!=2:
                l+=1
        return nums
