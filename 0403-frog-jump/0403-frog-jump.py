class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # use dp
        def bin_search(l, r, val):
            while l<=r:
                m=(l+r)//2
                if stones[m]==val:
                    return m
                elif stones[m]>val:
                    r=m-1
                else:
                    l=m+1
            return None
        @cache
        def dp(x, prev_unit):
            if x==len(stones)-1: return True
            cur_stone=stones[x]
            # use binary search to find the index for k-1,k,k+1
            res=False
            k=bin_search(x+1, len(stones)-1, cur_stone+prev_unit)
            if k:
                res=res or dp(k, prev_unit)
            k_plus=bin_search(x+1, len(stones)-1, cur_stone+prev_unit+1)
            if k_plus:
                res=res or dp(k_plus, prev_unit+1)
            k_minus=bin_search(x+1, len(stones)-1, cur_stone+prev_unit-1)
            if k_minus:
                res=res or dp(k_minus, prev_unit-1)
            return res
        if stones[1]!=stones[0]+1:
            return False
        return dp(1, 1)

