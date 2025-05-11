class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # use dijkstra on both src1 and src2 and maintain a global graph
        G=defaultdict(list)
        G_rev=defaultdict(list)
        for u, v, w in edges:
            G[u].append((v, w))
            G_rev[v].append((u, w))
        def dijk(src, g):
            dist=[inf]*n
            dist[src]=0
            q=[(0, src)]
            visited=set({})
            while q:
                w, node =heapq.heappop(q)
                if node in visited: continue
                visited.add(node)
                for neighbor, weight in g[node]:
                    if w+weight<dist[neighbor]:
                        dist[neighbor]=w+weight
                        heapq.heappush(q, (dist[neighbor], neighbor))
            return dist
        l1, l2, l3 = dijk(src1, G), dijk(src2, G), dijk(dest, G_rev)
        result=inf
        for i in range(len(l1)):
            result=min(result, l1[i]+l2[i]+l3[i])
        return result if result!=inf else -1