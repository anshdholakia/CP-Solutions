class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # 3 pointers approach
        # far, near, r
        # we will shift near if freq[nums[r]]>1
        # we will shift far and near if len(freq)>k
        far, near = 0, 0
        freq={}
        res=0
        for r in range(len(nums)):
            freq[nums[r]]=freq.get(nums[r],0)+1
            while len(freq)>k:
                freq[nums[near]]-=1
                if not freq[nums[near]]:
                    del freq[nums[near]]
                near+=1
                far=near
            while freq[nums[near]]>1 and len(freq)==k:
                freq[nums[near]]-=1
                near+=1
            if len(freq)==k:
                res+=(near-far+1)
        return res