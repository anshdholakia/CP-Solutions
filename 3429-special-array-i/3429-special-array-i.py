class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i]%2 and nums[i+1]%2:
                return False
            elif not nums[i]%2 and not nums[i+1]%2:
                return False
        return True