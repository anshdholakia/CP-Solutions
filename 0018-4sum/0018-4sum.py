class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        i=0
        while i<len(nums)-3:
            j=i+1
            while j<len(nums)-2:
                a, b = j+1, len(nums)-1
                new_t=target-nums[j]-nums[i]
                while a<b:
                    if nums[a]+nums[b]<new_t:
                        a+=1
                    elif nums[a]+nums[b]>new_t:
                        b-=1
                    else:
                        result.append([nums[i], nums[j], nums[a], nums[b]])
                        a+=1
                        b-=1
                        while a<b and nums[b]==nums[b+1]:
                            b-=1
                j+=1
                while j<len(nums)-2 and nums[j-1]==nums[j]:
                    j+=1
            i+=1
            while i<len(nums)-3 and nums[i-1]==nums[i]:
                i+=1
        return result
        