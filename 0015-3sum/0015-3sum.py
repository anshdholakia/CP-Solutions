class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        i = 0
        nums.sort()
        while i<len(nums)-2:
            nt = -nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r]==nt:
                    result.append([nums[i], nums[l], nums[r]])
                    # shift r till its diff
                    r-=1
                    while r>=0 and nums[r+1]==nums[r]:
                        r-=1
                    continue
                if nums[l]+nums[r]<nt:
                    l+=1
                else:
                    r-=1
            i+=1
            while i<len(nums)-2 and nums[i-1]==nums[i]:
                i+=1
        return result