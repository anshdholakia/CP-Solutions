class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # use a minheap to favor options with less obstacles
        visited=set({(0, 0)})
        minheap=[(0, 0, 0)]
        while minheap:
            popw, x, y = heapq.heappop(minheap)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return popw
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    heapq.heappush(minheap, (popw+(grid[x+dx][y+dy]==1), dx+x, y+dy))