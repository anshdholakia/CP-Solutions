class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        cur_i = 0
        total = 0
        while cur_i<len(nums)-1:
            for j in range(cur_i+1, len(nums)):
                if nums[j]>nums[cur_i]:
                    total+=nums[cur_i]*(j-cur_i)
                    cur_i=j
                    break
            else:
                total+=nums[cur_i]*(j-cur_i)
                break
        return total