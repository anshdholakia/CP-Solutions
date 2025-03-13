class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curs=0
        ps=defaultdict(int)
        ps[0]+=1
        res=0
        for n in nums:
            curs+=n
            res+=ps[curs-k]
            ps[curs]+=1
        return res