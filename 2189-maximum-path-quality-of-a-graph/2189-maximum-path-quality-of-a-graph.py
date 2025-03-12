class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        G=defaultdict(list)
        for u, v, w in edges:
            G[u].append((v, w))
            G[v].append((u, w))
        result=0
        def dfs(n, cur_tot, energy, visited):
            if n==0:
                nonlocal result
                result=max(result, cur_tot)
            visited.add(n)
            for neighbor, weight in G[n]:
                if energy-weight>=0:
                    if neighbor not in visited:
                        dfs(neighbor, cur_tot+values[neighbor], energy-weight, set(visited))
                    else:
                        dfs(neighbor, cur_tot, energy-weight, set(visited))
        dfs(0, values[0], maxTime, set())
        return result

