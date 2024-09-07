class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            cur_res = []
            for j in range(i):
                if j==0 or j==i-1:
                    cur_res.append(1)
                else:
                    cur_res.append(result[-1][j-1]+result[-1][j])
            result.append(cur_res)
        return result