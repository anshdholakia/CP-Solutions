class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        cnt=0
        ps=[0]
        for a, b in pairwise(nums):
            if (a+b)%2:
                cnt+=1
            ps.append(cnt)
        res=[]
        for l, r in queries:
            if ps[r]-ps[l]==r-l:
                res.append(True)
            else:
                res.append(False)
        return res