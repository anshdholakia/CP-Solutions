class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # modified bfs
        queue=collections.deque([(0, 0, 0)])
        steps=0
        visited=set({(0, 0, 0)})
        while queue:
            for _ in range(len(queue)):
                x, y, cur_k=queue.popleft()
                if x==len(grid)-1 and y==len(grid[0])-1:
                    return steps
                for dirx, diry in pairwise([-1,0,1,0,-1]):
                    if 0<=x+dirx<len(grid) and 0<=y+diry<len(grid[0]) and (x+dirx, y+diry, cur_k) not in visited:
                        if grid[x+dirx][y+diry]:
                            if cur_k+1<=k:
                                visited.add((x+dirx, y+diry, cur_k))
                                queue.append((x+dirx, y+diry, cur_k+1))
                        else:
                            visited.add((x+dirx, y+diry, cur_k))
                            queue.append((x+dirx, y+diry, cur_k))
            steps+=1
        return -1