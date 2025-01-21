class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top, bottom = sum(grid[0][1:]), 0
        max_val = max(top, bottom)
        for i in range(1, len(grid[0])):
            top-=grid[0][i]
            bottom+=grid[1][i-1]
            # since we are trying to minimize the value of max_val
            if max(top, bottom)<=max_val:
                max_val=max(top, bottom)
            else:
                break
        return max_val