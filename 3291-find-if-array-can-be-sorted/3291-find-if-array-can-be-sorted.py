class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i=0
        prev=0
        while i<len(nums):
            j=i+1
            mx,mn=nums[i],nums[i]
            cur_one=bin(nums[i]).count('1')
            while j<len(nums) and bin(nums[j]).count('1')==cur_one:
                mx=max(mx, nums[j])
                mn=min(mn, nums[j])
                j+=1
            if prev>mn:
                return False
            prev=mx
            i=j
        return True