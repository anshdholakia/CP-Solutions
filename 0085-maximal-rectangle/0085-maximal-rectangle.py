class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # this is similar to area of largest histogram
        # do the question for each row here
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c]=int(matrix[r][c])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] and row>0 and matrix[row-1][col]>=1:
                    matrix[row][col]+=matrix[row-1][col]
        result=0
        for row in range(len(matrix)):
            # for each row in matrix, consider the sub problem
            stack=[]
            matrix[row].append(-inf)
            # monotonic stack
            for i, h in enumerate(matrix[row]):
                cur_i=i
                while stack and stack[-1][0]>h:
                    height, i = stack.pop()
                    result=max(result, height*(cur_i-i))
                stack.append((h, i))
        return result
