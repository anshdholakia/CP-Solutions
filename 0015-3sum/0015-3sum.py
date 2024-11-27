class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            target=-nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                cur=nums[l]+nums[r]
                if cur==target:
                    res.append((nums[i], nums[l], nums[r]))
                if cur>target:
                    r-=1
                else:
                    l+=1
                    while 0<=l<r and nums[l-1]==nums[l]:
                        l+=1
        return res