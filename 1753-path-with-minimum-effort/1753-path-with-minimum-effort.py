class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap=[(0, 0, 0)]
        visited=set({})
        while heap:
            diff, x, y = heapq.heappop(heap)
            if x==len(heights)-1 and y==len(heights[0])-1:
                return diff
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dirx, diry in pairwise([-1,0,1,0,-1]):
                if 0<=dirx+x<len(heights) and 0<=diry+y<len(heights[0]):
                    heapq.heappush(heap, (max(diff, abs(heights[x][y]-heights[dirx+x][diry+y])), dirx+x, diry+y))
        
