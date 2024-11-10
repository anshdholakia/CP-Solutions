class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1:
            return sum(weights)
        l, r = 1, sum(weights)-1
        res=inf
        while l<=r:
            m=(l+r)//2
            # check m satisfies
            cur_w=0
            cdays=1
            for w in weights:
                if w>m:
                    cdays=inf
                    break
                cur_w+=w
                if cur_w>m:
                    cdays+=1
                    cur_w=w
            if cdays>days:
                l=m+1
            else:
                res=min(res, m)
                r=m-1
        return res