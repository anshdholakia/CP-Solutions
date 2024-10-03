class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        SUM = sum(nums)
        if not SUM%p:
            return 0
        need = SUM%p
        result = len(nums)
        cur_sum = 0
        ps = {0:-1} # key is cur_sum%p and value is index
        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n)%p
            new = (cur_sum - need + p)%p
            if new in ps:
                result=min(result, i-ps[new])
            ps[cur_sum] = i
        return -1 if result==len(nums) else result