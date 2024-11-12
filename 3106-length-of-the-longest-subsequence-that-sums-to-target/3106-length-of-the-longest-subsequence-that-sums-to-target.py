class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        cache=[[None]*(target+1) for _ in range(len(nums)+1)]
        def backtrack(x, cur_sum):
            if cur_sum==target:
                return 0
            if x==len(nums):
                return -inf
            if cur_sum>target:
                return -inf
            if cache[x][cur_sum]!=None:
                return cache[x][cur_sum]
            cache[x][cur_sum]=max(backtrack(x+1, cur_sum+nums[x])+1, backtrack(x+1, cur_sum))
            return cache[x][cur_sum]
        res=backtrack(0, 0)
        return res if res!=-inf else -1