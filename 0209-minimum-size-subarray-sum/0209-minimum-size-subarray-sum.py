class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums)+1
        l = 0
        curs = 0
        for r in range(len(nums)):
            curs+=nums[r]
            while curs>=target:
                result=min(result, r-l+1)
                curs-=nums[l]
                l+=1
        return 0 if result==len(nums)+1 else result