class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # eulerian path
        G=defaultdict(list)
        for u, v in tickets:
            G[u].append(v)
        for k in G:
            G[k].sort(reverse=True)
        res=[]
        def dfs(airport):
            while G[airport]:
                dfs(G[airport].pop())
            res.append(airport)
        dfs("JFK")
        return res[::-1]