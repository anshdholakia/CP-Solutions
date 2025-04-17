class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        output=[]
        while l<=r and t<=b:
            for i in range(l, r+1):
                output.append(matrix[t][i])
            t+=1
            if t>b:
                break
            for i in range(t, b+1):
                output.append(matrix[i][r])
            r-=1
            if l>r:
                break
            for i in range(r, l-1, -1):
                output.append(matrix[b][i])
            b-=1
            if t>b:
                break
            for i in range(b, t-1, -1):
                output.append(matrix[i][l])
            l+=1
        return output
