class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # do simulation but be smart while doing it
        # perform dfs to complete a riection for each guard and end the dfs when crossed a wall or another guard
        matrix=[[0]*n for _ in range(m)]
        for x, y in walls:
            matrix[x][y]=-1
        for x, y in guards:
            matrix[x][y]=1
        for x, y in guards:
            for dx, dy in pairwise([-1,0,1,0,-1]):
                nx,ny=dx+x,dy+y
                while 0<=nx<m and 0<=ny<n:
                    if matrix[nx][ny]==1 or matrix[nx][ny]==-1:
                        break
                    if matrix[nx][ny]==0:
                        matrix[nx][ny]=2
                    nx+=dx
                    ny+=dy
        unoccupied=0
        for x in range(m):
            for y in range(n):
                if matrix[x][y]==0:
                    unoccupied+=1
        return unoccupied