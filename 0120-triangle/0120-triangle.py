class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo=deepcopy(triangle)
        memo.append([0]*(len(memo[-1])+1))
        for row in range(len(memo)-2,-1,-1):
            for idx in range(len(memo[row])):
                memo[row][idx]=min(memo[row+1][idx]+triangle[row][idx], memo[row+1][idx+1]+triangle[row][idx])
        return memo[0][0]