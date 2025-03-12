class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        if ROWS==COLS:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i>=j:
                        continue
                    # swap
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        output=[[0]*ROWS for _ in range(COLS)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[j][i]=matrix[i][j]
        return output