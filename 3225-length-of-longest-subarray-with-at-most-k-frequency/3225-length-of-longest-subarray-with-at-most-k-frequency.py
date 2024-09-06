class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        result = 0
        cur_count = {}
        for r in range(len(nums)):
            cur_count[nums[r]] = cur_count.get(nums[r], 0) + 1
            while cur_count[nums[r]]>k:
                cur_count[nums[l]]-=1
                l+=1
            result = max(result, r-l+1)
        return result
