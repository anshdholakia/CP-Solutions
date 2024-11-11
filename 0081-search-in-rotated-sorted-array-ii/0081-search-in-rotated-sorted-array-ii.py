class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            if nums[l]<nums[m]:
                # left part is sorted
                if target<nums[l] or target>nums[m]:
                    l=m+1
                else:
                    r=m-1
            elif nums[l]>nums[m]:
                # right part is sorted
                if target<nums[m] or target>nums[r]:
                    r=m-1
                else:
                    l=m+1
            else:
                l+=1
        return False