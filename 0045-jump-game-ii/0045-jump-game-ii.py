class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r=0, 0
        steps=0
        while r<len(nums)-1:
            new_l=r+1
            for k in range(l, r+1):
                r=max(r, k+nums[k])
            l=new_l
            steps+=1
        return steps