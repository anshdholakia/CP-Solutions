class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # line sweep
        ps=defaultdict(int)
        lower, upper = inf, -inf
        for n in nums:
            lower=min(lower, n-k)
            ps[n-k]+=1
            ps[n+k+1]-=1
            upper=max(upper, n+k+1)
        cnt=0
        res=0
        for i in range(lower, upper+1):
            cnt+=ps[i]
            res=max(res, cnt)
        return res