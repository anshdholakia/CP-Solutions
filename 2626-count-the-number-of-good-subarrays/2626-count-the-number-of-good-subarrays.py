class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l=0
        cur_k=0
        count=defaultdict(int)
        result=0
        for r in range(len(nums)):
            cur_k+=count[nums[r]]
            count[nums[r]]+=1
            while cur_k>=k:
                result+=(len(nums)-r)
                count[nums[l]]-=1
                cur_k-=count[nums[l]]
                l+=1
        return result