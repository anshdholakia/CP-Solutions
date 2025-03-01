class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct the graph
        G=defaultdict(dict)
        for eq, val in zip(equations, values):
            G[eq[0]][eq[1]]=val
            G[eq[1]][eq[0]]=1/val
        visited=set({})
        def dfs(start, end):
            if start==end:
                return 1.0, True
            visited.add(start)
            res=-1.0
            ret=False
            for n, v in G[start].items():
                if n not in visited:
                    mult, rret = dfs(n, end)
                    if rret:
                        ret=True
                        res=max(res, v*mult)
            visited.remove(start)
            return res, ret
        res=[]
        for q1, q2 in queries:
            if q1 not in G or q2 not in G:
                res.append(-1)
                continue
            res.append(dfs(q1, q2)[0])
        return res