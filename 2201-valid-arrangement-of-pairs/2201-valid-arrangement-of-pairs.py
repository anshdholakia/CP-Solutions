class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        G=defaultdict(list)
        edge_count=defaultdict(int)
        for u, v in pairs:
            G[u].append(v)
            edge_count[u]+=1
            edge_count[v]-=1
        res=[]
        def dfs(n):
            if not G[n]:
                res.append(n)
                return
            while G[n]:
                dfs(G[n].pop())
            res.append(n)
        start=pairs[0][0]
        for k, v in edge_count.items():
            if v==1:
                start=k
        dfs(start)
        res.reverse()
        return [[res[i], res[i+1]] for i in range(len(res)-1)]