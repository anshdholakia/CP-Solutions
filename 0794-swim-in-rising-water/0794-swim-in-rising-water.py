class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[(grid[0][0], 0, 0)]
        visited=set()
        visited.add((0, 0))
        while heap:
            val, x, y = heapq.heappop(heap)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return val
            for dirx, diry in pairwise([-1,0,1,0,-1]):
                if 0<=x+dirx<len(grid) and 0<=y+diry<len(grid[0]) and (x+dirx, y+diry) not in visited:
                    visited.add((x+dirx, y+diry))
                    heapq.heappush(heap, (max(val, grid[x+dirx][y+diry]), x+dirx, y+diry))