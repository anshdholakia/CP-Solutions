class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps, suff = 0, sum(nums)
        res=[]
        for i, x in enumerate(nums):
            ps+=x
            suff-=x
            res.append((x*(i+1)-ps)+(suff-x*(len(nums)-i-1)))
        return res