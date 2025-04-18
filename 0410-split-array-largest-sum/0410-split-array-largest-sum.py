class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total=sum(nums)
        l, r = 0, total
        ans=0
        def check(mid):
            curs=0
            array=1
            for i in range(len(nums)):
                curs+=nums[i]
                if nums[i]>mid:
                    return False
                if curs>mid:
                    curs=nums[i]
                    array+=1
            return array<=k
        while l<=r:
            m=(l+r)//2
            if check(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans