class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        curs=1
        for x in nums:
            prefix.append(curs)
            curs*=x
        curs=1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] = prefix[i]*curs
            curs = nums[i]*curs
        return prefix