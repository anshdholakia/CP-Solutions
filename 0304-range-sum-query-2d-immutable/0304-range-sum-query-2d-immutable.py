class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(self.dp)):
            for j in range(1, len(self.dp[0])):
                self.dp[i][j]=matrix[i-1][j-1]+self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]
        print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cur_sum = self.dp[row2+1][col2+1]
        cur_sum -= self.dp[row1][col2+1]
        cur_sum -= self.dp[row2+1][col1]
        cur_sum += self.dp[row1][col1]
        return cur_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)