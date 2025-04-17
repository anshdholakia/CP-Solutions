class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while l<r and t<b:
            for i in range(r-l):
                prev=matrix[t][l+i]
                matrix[t][l+i]=matrix[b-i][l]
                matrix[b-i][l]=matrix[b][r-i]
                matrix[b][r-i]=matrix[t+i][r]
                matrix[t+i][r]=prev
            l+=1
            r-=1
            t+=1
            b-=1