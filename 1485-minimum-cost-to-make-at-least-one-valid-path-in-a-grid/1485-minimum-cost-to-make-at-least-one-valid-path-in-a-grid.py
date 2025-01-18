class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # dijkstras
        minheap=[(0, 0, 0)] # (cost, x, y)
        visited=set({})
        while minheap:
            cost, x, y = heapq.heappop(minheap)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return cost
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dirx, diry in pairwise([-1,0,1,0,-1]):
                if 0<=x+dirx<len(grid) and 0<=y+diry<len(grid[0]) and (x+dirx, y+diry) not in visited: 
                    if grid[x][y]==1:
                        if dirx==0 and diry==1:
                            heapq.heappush(minheap, (cost, x+dirx, y+diry))
                        else:
                            heapq.heappush(minheap, (cost+1, x+dirx, y+diry))
                    elif grid[x][y]==2:
                        if dirx==0 and diry==-1:
                            heapq.heappush(minheap, (cost, x+dirx, y+diry))
                        else:
                            heapq.heappush(minheap, (cost+1, x+dirx, y+diry))
                    elif grid[x][y]==3:
                        if dirx==1 and diry==0:
                            heapq.heappush(minheap, (cost, x+dirx, y+diry))
                        else:
                            heapq.heappush(minheap, (cost+1, x+dirx, y+diry))
                    elif grid[x][y]==4:
                        if dirx==-1 and diry==0:
                            heapq.heappush(minheap, (cost, x+dirx, y+diry))
                        else:
                            heapq.heappush(minheap, (cost+1, x+dirx, y+diry))
                
            

                
