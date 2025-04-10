class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                tot=nums[l]+nums[r]
                if tot<-nums[i]:
                    l+=1
                elif tot>-nums[i]:
                    r-=1
                else:
                    result.append((nums[i], nums[l], nums[r]))
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
        return result