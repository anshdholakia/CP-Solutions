class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time=[t%60 for t in time]
        ps={}
        res=0
        for key in time:
            if key==0:
                res+=ps.get(key,0)
            else:
                res+=ps.get(60-key,0)
            ps[key]=ps.get(key,0)+1
        return int(res)