class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # use 2d prefix sum
        ans=-inf
        ps=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<=k:
                    ans=max(ans, matrix[i][j])
                ps[i][j]=matrix[i][j]+(ps[i-1][j] if i>0 else 0)+(ps[i][j-1] if j>0 else 0)-(ps[i-1][j-1] if i>0 and j>0 else 0)
        for left in range(len(ps[0])):
            for right in range(left, len(ps[0])):
                sorted_sums=[0]
                for row in range(len(ps)):
                    cur_sum=ps[row][right]-(ps[row][left-1] if left>0 else 0)
                    target=cur_sum-k
                    pos=bisect.bisect_left(sorted_sums, target)
                    if pos < len(sorted_sums):
                        ans=max(ans, cur_sum-sorted_sums[pos])
                    bisect.insort(sorted_sums, cur_sum)
        return ans