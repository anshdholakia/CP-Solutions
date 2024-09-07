class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = 0
        for i in range(len(nums)-1):
            if not change%2:
                if nums[i+1]<nums[i]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            elif nums[i+1]>nums[i]:
                nums[i+1], nums[i]=nums[i], nums[i+1]
            change+=1





                    