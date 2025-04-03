class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            # use i as k and get the max and min
            minimum=nums[i-1]
            max_sum=-inf
            for j in range(i-2, -1, -1):
                max_sum=max(max_sum, nums[j]-minimum)
                minimum=min(minimum, nums[j])
            result=max(result, max_sum*nums[i])
        return result