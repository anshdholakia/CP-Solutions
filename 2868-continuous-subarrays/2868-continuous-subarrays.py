class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res=0
        l=0
        hashmap={}
        for r in range(len(nums)):
            hashmap[nums[r]]=hashmap.get(nums[r],0)+1
            while abs(max(hashmap)-min(hashmap))>2:
                hashmap[nums[l]]-=1
                if not hashmap[nums[l]]:
                    del hashmap[nums[l]]
                l+=1
            res+=(r-l+1)
        return res