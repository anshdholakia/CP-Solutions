class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i>0 and nums[i-1]<nums[i]:
                break
        if i==0:
            nums.reverse()
            return 
        # get the smallest digit which is greater than i-1
        idx=i
        for k in range(i, len(nums)):
            if nums[i-1]<nums[k]<=nums[idx]:
                idx=k
        # swap the numbers
        nums[i-1], nums[idx] = nums[idx], nums[i-1]
        # reverse the order to make it smaller
        l, r = i, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            r-=1
            l+=1
        