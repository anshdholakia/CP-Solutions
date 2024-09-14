class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_elem = max(nums)
        count = 0
        result = 0
        for n in nums:
            if n==max_elem:
                count+=1
            else:
                count=0
            result=max(result, count)
        return result