class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # find the dominant element
        map=collections.Counter(nums)
        key, cur_v = None, -inf
        for k, v in map.items():
            if v>cur_v:
                key=k
                cur_v=v
        # select the breaking point in the array
        cur_count=0
        for i in range(len(nums)):
            if nums[i]==key:
                cur_count+=1
            if cur_count>(i+1)//2 and cur_v-cur_count>(len(nums)-i-1)//2:
                return i
        return -1
