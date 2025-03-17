class Solution:
    def maxSum(self, nums: List[int]) -> int:
        #kadane+sliding window
        cur_sum=0
        l=0
        result=max(nums)
        visited=set({})
        for r in range(len(nums)):
            if nums[r]<0 or nums[r] in visited:
                continue
            cur_sum+=nums[r]
            visited.add(nums[r])
            result=max(result, cur_sum)
        return result
