class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        # use the nums to store the results
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]*=-1
        return res