class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time=[t%60 for t in time]
        ps={}
        res=0
        for t in time:
            if t==0:
                res+=ps.get(0,0)
            else:
                res+=ps.get(60-t,0)
            ps[t]=ps.get(t,0)+1
        return res