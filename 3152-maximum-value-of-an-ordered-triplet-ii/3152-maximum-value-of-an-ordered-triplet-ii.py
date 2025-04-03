class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        prev_max = nums[0]
        result=0
        for i in range(1, len(nums)):
            result=max(result, max_diff*nums[i])
            max_diff=max(max_diff, prev_max-nums[i])
            prev_max=max(prev_max, nums[i])
        return result