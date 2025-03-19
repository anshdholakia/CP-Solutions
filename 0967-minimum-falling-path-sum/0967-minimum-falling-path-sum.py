class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                val=matrix[row][c]
                matrix[row][c]=inf
                for d in [-1,0,1]:
                    if 0<=c+d<len(matrix[0]):
                        matrix[row][c]=min(matrix[row][c], val+matrix[row-1][c+d])
        return min(matrix[-1])