class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # use cyclic sort
        # replace all negatives with zeros
        n=len(nums)
        for i, x in enumerate(nums):
            if x<0:
                nums[i]=0
        for x in range(len(nums)):
            if nums[x]!=0 and abs(nums[x])-1<n:
                if nums[abs(nums[x])-1]>0:
                    nums[abs(nums[x])-1]*=-1
                elif nums[abs(nums[x])-1]==0:
                    nums[abs(nums[x])-1]=-n
        for i in range(n):
            if nums[i]>=0:
                return i+1
        return n+1