class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        to_remove = []
        for i, n in enumerate(nums):
            if n==0:
                to_remove.append(i)
        nums+=[0]*len(to_remove)
        removed=0
        for i in to_remove:
            nums.pop(i-removed)
            removed+=1
        return nums