class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        cur_sum = 0
        result = 0
        for n in nums:
            cur_sum+=n
            if cur_sum-k in prefixSums:
                result+=prefixSums[cur_sum-k]
            prefixSums[cur_sum]=prefixSums.get(cur_sum, 0)+1
        return result