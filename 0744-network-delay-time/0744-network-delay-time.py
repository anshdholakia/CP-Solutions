class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        time=0
        visited=set({})
        minheap=[(0, k)]
        while minheap and len(visited)!=n:
            while minheap and minheap[0][0]==time:
                _, node=heapq.heappop(minheap)
                if node in visited:
                    continue
                visited.add(node)
                if len(visited)==n:
                    return time
                for neighbor, weight in G[node]:
                    if neighbor not in visited:
                        heapq.heappush(minheap, (weight+time, neighbor))
            time+=1
        return time if len(visited)==n else -1