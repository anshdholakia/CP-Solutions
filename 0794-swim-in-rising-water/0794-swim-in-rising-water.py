class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap=[(grid[0][0], 0, 0)]
        visited=set({})
        max_val=-inf
        while minheap:
            d, x, y = heapq.heappop(minheap)
            max_val=max(max_val, grid[x][y])
            if x==len(grid)-1 and y==len(grid[0])-1:
                return max_val
            visited.add((x, y))
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and (dx+x, y+dy) not in visited:
                    visited.add((dx+x, dy+y))
                    heapq.heappush(minheap, (grid[dx+x][y+dy], dx+x, dy+y))
