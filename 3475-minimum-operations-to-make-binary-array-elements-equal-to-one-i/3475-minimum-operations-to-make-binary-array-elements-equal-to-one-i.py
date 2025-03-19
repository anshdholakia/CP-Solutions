class Solution:
    def minOperations(self, nums: List[int]) -> int:
        idx=0
        ops=0
        while idx<len(nums)-2:
            if nums[idx]==0:
                ops+=1
                for i in range(idx, idx+3):
                    nums[i]^=1
            idx+=1
        while idx<len(nums):
            if not nums[idx]:
                return -1
            idx+=1
        return ops