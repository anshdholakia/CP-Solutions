class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(max_val):
            cur_k=1
            cur_s=0
            for i in range(len(nums)):
                cur_s+=nums[i]
                if cur_s>max_val:
                    cur_s=nums[i]
                    cur_k+=1
            return cur_k
        # do binary search on the max of the nums and sum of nums
        l, r = max(nums), sum(nums)
        res=r
        while l<=r:
            m=(l+r)//2
            if check(m)<=k:
                res=m
                r=m-1
            else:
                l=m+1
        return res