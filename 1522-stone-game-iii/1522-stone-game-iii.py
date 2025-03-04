class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # min-max algorithm
        @cache
        def dfs(i):
            if i==len(stoneValue):
                return 0
            res=-inf
            for k in range(i, min(len(stoneValue), i+3)):
                res=max(res, sum(stoneValue[i:k+1])-dfs(k+1))
            return res
        r=dfs(0)
        if r>0:
            return "Alice"
        elif r<0:
            return "Bob"
        return "Tie"