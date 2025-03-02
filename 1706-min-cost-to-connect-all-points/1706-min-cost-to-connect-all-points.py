class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        init=tuple(points[0])
        points=set([tuple(x) for x in points])
        heap=[(0, init[0], init[1])]
        visited=set({})
        res=0
        while heap:
            v, x, y = heapq.heappop(heap)
            if (x, y) in points:
                res+=v
                points.remove((x, y))
                for dirx, diry in points:
                    heapq.heappush(heap, (abs(x-dirx)+abs(y-diry), dirx, diry))
        return res