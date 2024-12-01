class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=[(v, k) for k, v in collections.Counter(nums).items()]
        def quickselect(l, r):
            pvt=r
            r-=1
            while l<=r:
                if nums[l][0]>nums[pvt][0] and nums[r][0]<nums[pvt][0]:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
                if nums[l][0]<=nums[pvt][0]:
                    l+=1
                if nums[r][0]>=nums[pvt][0]:
                    r-=1
            nums[l], nums[pvt] = nums[pvt], nums[l]
            return l
        l, r = 0, len(nums)-1
        k=len(nums)-k
        while True:
            curk=quickselect(l, r)
            if curk==k:
                return [x[1] for x in nums[curk:]]
            elif curk<k:
                l=curk+1
            else:
                r=curk-1
        