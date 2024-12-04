class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                new_t=target-nums[i]-nums[j]
                x, y = j+1, len(nums)-1
                while x<y:
                    if nums[x]+nums[y]==new_t:
                        result.append((nums[i], nums[j], nums[x], nums[y]))
                        x+=1
                        while x<y and nums[x]==nums[x-1]:
                            x+=1
                    elif nums[x]+nums[y]<new_t:
                        x+=1
                    else:
                        y-=1
        return result
