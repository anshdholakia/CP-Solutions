class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        memo=defaultdict(list)
        @cache
        def dp(idxMap, prev):
            if idxMap==((1<<n)-1):
                return abs(nums[0]-prev)
            finalVal, minVal = inf, -1
            for i in range(len(nums)):
                if idxMap&(1<<i)==0:
                    curVal=abs(nums[i]-prev)+dp(idxMap|(1<<i), i)
                    if curVal<finalVal:
                        minVal, finalVal = i, curVal
            memo[(idxMap, prev)]=[minVal]+memo[(idxMap|(1<<minVal), minVal)]
            return finalVal
        dp(1, 0)
        return [0]+memo[(1, 0)]
            
