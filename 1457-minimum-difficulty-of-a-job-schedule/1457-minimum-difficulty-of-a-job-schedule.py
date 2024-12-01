class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # you need to basically do dp on i and current d
        @cache
        def dp(x, day):
            if day==d:
                return 0 if x==len(jobDifficulty) else inf
            if x==len(jobDifficulty):
                return inf
            # you either decide to break from here or keep continuing
            res=inf
            max_elem=jobDifficulty[x]
            for k in range(x, len(jobDifficulty)):
                max_elem=max(max_elem, jobDifficulty[k])
                res=min(res, max_elem+dp(k+1, day+1))
            return res
        res=dp(0, 0)
        return res if res!=inf else -1
