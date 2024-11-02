class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if (nums[m-1] if m>0 else -inf)<nums[m]>(nums[m+1] if m<len(nums)-1 else -inf):
                return m
            if m>0 and nums[m-1]>nums[m]:
                r=m-1
            elif m<len(nums)-1 and nums[m]<nums[m+1]:
                l=m+1
        return m
            