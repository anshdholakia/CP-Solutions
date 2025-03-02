class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        visited=set({})
        heap=[(0, k)]
        while heap:
            time = heap[0][0]
            while heap and heap[0][0]==time:
                _, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for neigh, weight in G[node]:
                    if neigh not in visited:
                        heapq.heappush(heap, (weight+time, neigh))
            if len(visited)==n:
                return time
        return -1