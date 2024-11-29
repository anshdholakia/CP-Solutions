class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        minheap=[(0, 0, 0)]
        visited=set({(0, 0)})
        # check if the origin has any where to go or not
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        while minheap:
            w, x, y = heapq.heappop(minheap)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return w
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and (dx+x, dy+y) not in visited:
                    visited.add((dx+x, dy+y))
                    heapq.heappush(minheap, (max(1+w, grid[dx+x][dy+y]+((grid[dx+x][dy+y]-w)%2==0)), dx+x, dy+y))
        return -1