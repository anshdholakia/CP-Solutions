class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []
        def backtrack(x):
            if x==len(nums):
                result.append(current.copy())
                return
            current.append(nums[x])
            backtrack(x+1)
            current.pop()
            while x+1<len(nums) and nums[x]==nums[x+1]:
                x+=1
            backtrack(x+1)
        backtrack(0)
        return result