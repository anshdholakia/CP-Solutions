class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cur_sum=0
        hashset=set({})
        l=0
        for r in range(len(nums)):
            while nums[r] in hashset or len(hashset)==k:
                cur_sum-=nums[l]
                hashset.remove(nums[l])
                l+=1
            hashset.add(nums[r])
            cur_sum+=nums[r]
            if r-l+1==k:
                res=max(res, cur_sum)
        return res
