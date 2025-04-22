class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G=defaultdict(list)
        for u, v, w in flights:
            G[u].append((v, w))
        minheap=[(0, -1, src)]
        visited=set({})
        while minheap:
            distance, cur_k, node = heapq.heappop(minheap)
            if node==dst:
                return distance
            if cur_k==k:
                continue
            if (cur_k, node) in visited:
                continue
            visited.add((cur_k, node))
            for neighbor, weight in G[node]:
                if (cur_k+1, neighbor) not in visited:
                    heapq.heappush(minheap, (distance+weight, cur_k+1, neighbor))
        return -1