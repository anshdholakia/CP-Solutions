class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # maximize alices first turn but then minimize it
        memo={}
        def dp(i, alice, M):
            if i==len(piles):
                return 0
            if (i, alice, M) in memo:
                return memo[(i, alice, M)]
            cur_res=0
            res=0 if alice else inf
            for X in range(0, 2*M):
                if i+X>=len(piles):
                    break
                cur_res+=piles[i+X]
                if alice:
                    res=max(res, cur_res+dp(i+X+1, not alice, max(M, X+1)))
                else:
                    res=min(res, dp(i+X+1, not alice, max(M, X+1)))
            memo[(i, alice, M)]=res
            return res
        return dp(0, True, 1)