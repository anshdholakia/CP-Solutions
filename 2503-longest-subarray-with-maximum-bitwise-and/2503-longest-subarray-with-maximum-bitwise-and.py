class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur_result = None
        max_length = 0
        cur_length = 0
        k = -float("inf")
        for n in nums:
            if cur_result!=None and (cur_result>(cur_result&n) or n>cur_result):
                cur_result = None
                cur_length = 0
            cur_result = (cur_result & n) if cur_result!=None else n
            cur_length += 1
            if cur_result>k:
                max_length = cur_length
                k = cur_result
            elif cur_result==k:
                max_length = max(max_length, cur_length)
        return max_length
