class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x):
            # check if you can make subarray under k with max sum of x
            cur_sum=0
            cur_k=1
            for n in nums:
                cur_sum+=n
                if cur_sum>x:
                    cur_sum=n
                    if cur_sum>x:
                        return False
                    cur_k+=1
            return cur_k<=k
        l, r = max(nums), sum(nums)
        res=-1
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res