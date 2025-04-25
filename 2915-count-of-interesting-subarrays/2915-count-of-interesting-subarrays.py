class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ps=[]
        cnt=0
        for i in range(len(nums)):
            if nums[i]%modulo==k:
                cnt+=1
            ps.append(cnt)
        # find the subarry which ends at i such that
        # ps[i]-x%modulo=k
        res=0
        last_idx={0:1}
        for i in range(len(ps)):
            REM=ps[i]%modulo
            if (REM-k)%modulo in last_idx: res+=last_idx[(REM-k)%modulo]
            last_idx[ps[i]%modulo]=last_idx.get(ps[i]%modulo,0)+1
        return res

        