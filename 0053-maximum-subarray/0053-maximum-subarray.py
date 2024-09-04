class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_sum = float("-inf")
        cur_sum = 0
        for n in nums:
            if cur_sum+n<0:
                cur_sum=0
            else:
                cur_sum+=n
                final_sum = max(final_sum, cur_sum)
            final_sum = max(final_sum, n)
        return final_sum
