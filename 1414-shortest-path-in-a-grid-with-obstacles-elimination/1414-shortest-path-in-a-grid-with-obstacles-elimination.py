class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited=set({(0, 0, k)})
        queue=collections.deque([(0, 0, k, 0)])
        level=-1
        res=inf
        while queue:
            level+=1
            for _ in range(len(queue)):
                x, y, popk, popw = queue.popleft()
                if x==len(grid)-1 and y==len(grid[0])-1:
                    return popw
                for dx, dy in pairwise([-1,0,1,0,-1]):
                    if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and (dx+x, dy+y, popk) not in visited:
                        visited.add((dx+x,dy+y,popk))
                        if grid[dx+x][dy+y]==1 and popk:
                            queue.append((dx+x, dy+y, popk-1, popw+1))
                        elif grid[dx+x][dy+y]==0:
                            queue.append((dx+x, dy+y, popk, popw+1))
        return -1