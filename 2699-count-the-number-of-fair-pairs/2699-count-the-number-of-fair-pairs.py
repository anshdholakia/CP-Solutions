class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sort the array and for each of the numbers find a range using binary search which keeps the sum in bounds
        nums.sort()
        def large_binary_search(i, l, r):
            res=inf
            while l<=r:
                m=(l+r)//2
                if nums[m]+nums[i]<=upper:
                    res=m
                    l=m+1
                else:
                    r=m-1
            return res
        def small_binary_search(i, l, r):
            res=inf
            while l<=r:
                m=(l+r)//2
                if nums[m]+nums[i]>=lower:
                    res=m
                    r=m-1
                else:
                    l=m+1
            return res
        final=0
        for i in range(len(nums)):
            l, r = small_binary_search(i, i+1, len(nums)-1), large_binary_search(i, i+1, len(nums)-1)
            if l!=inf and r!=inf:
                final+=(r-l+1)
        return final