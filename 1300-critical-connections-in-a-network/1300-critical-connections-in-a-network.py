class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # tarjans algorithm
        G = defaultdict(list)
        for u, v in connections:
            G[u].append(v)
            G[v].append(u)
        lowest_discovery=[n]*n
        critical=[]
        def dfs(node, discovery_time, parent):
            if lowest_discovery[node]==n:
                lowest_discovery[node]=discovery_time
                for nei in G[node]:
                    if nei!=parent:
                        expected_discovery_time=discovery_time+1
                        actual_discovery_time=dfs(nei, discovery_time+1, node)
                        if actual_discovery_time>=expected_discovery_time:
                            critical.append((node, nei))
                        lowest_discovery[node]=min(lowest_discovery[node], actual_discovery_time)
            return lowest_discovery[node]
        dfs(0, 0, 0)
        return critical