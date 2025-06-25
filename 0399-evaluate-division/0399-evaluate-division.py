class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G=defaultdict(list)
        for (u, v), w in zip(equations, values):
            G[u].append((v, w))
            G[v].append((u, 1/w))
        visited=set({})
        def dfs(node, end):
            if node not in G or end not in G:
                return -1.0
            if node==end:
                return 1.0
            visited.add(node)
            res=-inf
            for neighbor, weight in G[node]:
                if neighbor not in visited:
                    res=max(res, weight*dfs(neighbor, end))
            visited.remove(node)
            return res
        return [max(-1, dfs(s, e)) for s, e in queries]
        