class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ps=[]
        cs=0
        for i, c in enumerate(s):
            if c=='*':
                cs+=1
            ps.append(cs)
        lplate, rplate = [], []
        closel=len(s)-1
        for i in range(len(s)-1, -1, -1):
            if s[i]=='|':
                closel=i
            rplate.append(closel)
        rplate=rplate[::-1]
        closel=0
        for i in range(len(s)):
            if s[i]=='|':
                closel=i
            lplate.append(closel)
        res=[]
        for l, r in queries:
            plates=ps[lplate[r]]-ps[rplate[l]]
            res.append(max(0, plates))
        return res