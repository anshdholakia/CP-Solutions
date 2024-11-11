class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # this is simple 2d dp
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                opt1, opt2 = inf, inf
                if i>0:
                    opt1=grid[i-1][j]
                if j>0:
                    opt2=grid[i][j-1]
                grid[i][j]=min(grid[i][j]+opt1, grid[i][j]+opt2) if min(opt1, opt2)!=inf else grid[i][j]
        return grid[-1][-1]