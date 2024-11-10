class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pvt=None
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1]>nums[i]:
                pvt=i
                break
        if pvt==None:
            nums.reverse()
            return
        # find the closest minimum number to swap with
        min_idx=pvt+1
        for i in range(pvt+1, len(nums)):
            if nums[pvt]<nums[i]<nums[min_idx]:
                min_idx=i
        # swap pvt with min_idx
        nums[pvt], nums[min_idx] = nums[min_idx], nums[pvt]
        # put all the remaining elements in sorted order
        rem = sorted(nums[pvt+1:])
        for i in range(pvt+1, len(nums)):
            nums[i]=rem[i-pvt-1]

        
        