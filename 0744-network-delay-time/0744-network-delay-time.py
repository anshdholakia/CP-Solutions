class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((w, v))
        result = -1
        heap = [(0, k)]
        visited = set({})
        while heap:
            result = heap[0][0]
            while heap and heap[0][0]==result:
                popw, popn = heapq.heappop(heap)
                if popn in visited:
                    continue
                visited.add(popn)
                if len(visited)==n:
                    break
                for w, neigh in G[popn]:
                    if neigh not in visited:
                        heapq.heappush(heap, (popw+w, neigh))
            if len(visited)==n:
                break
        return result if len(visited)==n else -1