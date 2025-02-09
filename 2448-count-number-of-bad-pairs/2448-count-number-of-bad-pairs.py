class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total=len(nums)*(len(nums)-1)/2
        count=defaultdict(int)
        for i, n in enumerate(nums):
            count[n-i]+=1
        good=0
        for k, v in count.items():
            if v!=1:
                good+=((v-1)*v)//2
        return int(total-good)