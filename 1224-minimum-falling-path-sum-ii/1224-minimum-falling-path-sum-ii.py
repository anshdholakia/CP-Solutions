class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # keep the min1, min2 for each row above
        dp=grid[0]
        for row in range(1, len(grid)):
            min1, min2 = inf, inf
            for val in dp:
                if val<min1:
                    min1, min2=val, min1
                elif val<min2:
                    min2=val
            for c in range(len(grid)):
                if min1==grid[row-1][c]:
                    grid[row][c]+=min2
                else:
                    grid[row][c]+=min1
            dp=grid[row]
        return min(dp)