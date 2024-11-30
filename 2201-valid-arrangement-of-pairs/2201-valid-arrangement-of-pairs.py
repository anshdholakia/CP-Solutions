class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # outgoing - incoming edges.
        # euler's path
        G_out=defaultdict(list)
        G_in=defaultdict(list)
        for u, v in pairs:
            G_out[u].append(v)
            G_in[v].append(u)
        start=u
        # find the node with the outgoing - incoming = 1
        for node in G_out:
            if len(G_out[node])-len(G_in[node])==1:
                start=node
                break
        # do euler's path
        res=[]
        def dfs(node):
            while G_out[node]:
                dfs(G_out[node].pop())
            res.append(node)
        dfs(start)
        res=res[::-1]
        return [[res[i], res[i+1]] for i in range(len(res)-1)]

        