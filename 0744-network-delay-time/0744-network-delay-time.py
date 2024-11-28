class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        visited=set({})
        minheap=[(0, k)]
        while minheap:
            minw=minheap[0][0]
            while minheap and minheap[0][0]==minw:
                w, node = heapq.heappop(minheap)
                if node in visited:
                    continue
                visited.add(node)
                for neighbor, weight in G[node]:
                    if neighbor not in visited:
                        heapq.heappush(minheap, (minw+weight, neighbor))
            if len(visited)>=n:
                return minw
        return -1