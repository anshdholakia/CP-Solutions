class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstras
        G = defaultdict(list)
        for fro, to, price in flights:
            G[fro].append((price, to))
        power = {i:float("inf") for i in range(n)}
        power[src]=0
        minheap = [(0, src, 0)]
        while minheap:
            popk, popn, popw = heapq.heappop(minheap)
            if popk>k:
                continue
            for w, n in G[popn]:
                if power[n]>popw+w:
                    power[n]=popw+w
                    heapq.heappush(minheap, (popk+1, n, power[n]))
        return power[dst] if power[dst]!=float("inf") else -1
            