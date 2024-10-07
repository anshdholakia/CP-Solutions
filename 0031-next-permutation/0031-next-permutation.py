class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1]>nums[i]:
                break
        else:
            nums.reverse()
            return
        # find the replacement
        j=i
        minimum = float("inf")
        min_index=j
        for i in range(j+1, len(nums)):
            if nums[i]>nums[j] and minimum>nums[i]:
                minimum=nums[i]
                min_index=i
        # swap
        nums[j], nums[min_index] = nums[min_index], nums[j]
        # do insert sort on the rest
        for i in range(j+1, len(nums)):
            min_val = (i, nums[i])
            for j in range(i+1, len(nums)):
                if min_val[1]>nums[j]:
                    min_val = (j, nums[j])
            nums[min_val[0]], nums[i] = nums[i], nums[min_val[0]]
        