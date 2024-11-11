class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dijkstra
        visited = set({(0, 0)})
        minheap=[(grid[0][0], 0, 0)]
        while minheap:
            val, x, y = heapq.heappop(minheap)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return val
            for dx, dy in [(0, 1), (1, 0)]:
                if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and (dx+x, dy+y) not in visited:
                    visited.add((dx+x, dy+y))
                    heapq.heappush(minheap, (val+grid[dx+x][dy+y], dx+x, dy+y))