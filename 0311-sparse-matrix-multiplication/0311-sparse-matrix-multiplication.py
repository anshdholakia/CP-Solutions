class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result=[[0]*len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(result)):
            for j in range(len(result[0])):
                cur_sum=0
                for k in range(len(mat1[0])):
                    cur_sum+=mat1[i][k]*mat2[k][j]
                result[i][j]=cur_sum
        return result