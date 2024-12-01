class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        @cache
        def dp(left, right, cut_l, cut_r):
            if cut_l>cut_r:
                return 0
            res=inf
            for k in range(cut_l, cut_r+1):
                if left<=cuts[k]<=right:
                    res=min(res, right-left+dp(left, cuts[k], cut_l, k-1)+dp(cuts[k], right, k+1, cut_r))
            return res
        return dp(0, n, 0, len(cuts)-1)