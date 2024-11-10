class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # put all negatives as zeros
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=len(nums)+1
            elif nums[i]<0:
                nums[i]=0
        # mark all indices here
        for n in nums:
            if 0<=abs(n)-1<len(nums):
                if nums[abs(n)-1]>0:
                    nums[abs(n)-1]*=-1
                elif nums[abs(n)-1]==0:
                    nums[abs(n)-1]=-(len(nums)+1)
        # check closest n
        for n in range(1, len(nums)+1):
            if nums[n-1]>=0:
                return n
        return n+1