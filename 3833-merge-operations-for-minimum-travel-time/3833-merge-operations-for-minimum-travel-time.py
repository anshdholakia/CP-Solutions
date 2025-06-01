class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        prefix=time.copy()
        for i in range(1, n):
            prefix[i]+=prefix[i-1]
        @cache
        def dp(i, left_k, cur_time):
            if i==n-1:
                return 0 if left_k==0 else inf
            res=(position[i+1]-position[i])*cur_time+dp(i+1, left_k, prefix[i+1]-prefix[i])
            for k in range(1, n):
                next_i = i+k+1
                if next_i>=n:
                    continue
                tmp=(position[next_i]-position[i])*cur_time+dp(next_i, left_k-k, prefix[next_i]-prefix[i])
                res=min(res, tmp)
            return res
        return dp(0, k, time[0])