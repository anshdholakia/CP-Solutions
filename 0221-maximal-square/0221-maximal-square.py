class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    matrix[i][j]=1+min((matrix[i-1][j-1] if i>0 and j>0 else 0), (matrix[i-1][j] if i>0 else 0), (matrix[i][j-1] if j>0 else 0))
                    res=max(res, matrix[i][j])
                else:
                    matrix[i][j]=int(matrix[i][j])
        return res**2