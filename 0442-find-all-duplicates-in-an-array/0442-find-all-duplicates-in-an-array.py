class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            n = abs(n)
            if nums[n-1]<0:
                output.append(n)
            nums[n-1]*=-1
        return output