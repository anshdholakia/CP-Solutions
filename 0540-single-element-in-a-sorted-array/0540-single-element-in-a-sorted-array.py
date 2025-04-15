class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if (nums[m-1] if m>0 else inf)!=nums[m]!=(nums[m+1] if m+1<len(nums) else inf):
                return nums[m]
            leftSize=m-1 if (m>0 and nums[m-1]==nums[m]) else m
            if leftSize%2:
                r=m-1
            else:
                l=m+1