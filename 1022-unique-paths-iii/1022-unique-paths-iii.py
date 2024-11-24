class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        EMPTY=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    EMPTY+=1
        def dfs(i, j, rem):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==-1:
                return 0
            if grid[i][j]==2:
                return 1 if rem==0 else 0
            grid[i][j]=-1
            paths=dfs(i+1, j, rem-1)+dfs(i, j+1, rem-1)+dfs(i-1, j, rem-1)+dfs(i, j-1, rem-1)
            grid[i][j]=0
            return paths
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i, j, EMPTY)