class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        heapq.heapify(nums)
        neg_nums=[-x for x in nums]
        heapq.heapify(neg_nums)
        res=inf
        popped=[]
        for _ in range(3):
            popped.append(heapq.heappop(neg_nums))
        for i in range(3):
            # pop i from nums
            # pop 3-i from neg_nums
            res=min(res, -neg_nums[0]-nums[0])
            heapq.heappop(nums)
            heapq.heappush(neg_nums, popped.pop())
            res=min(res, -neg_nums[0]-nums[0])
        return res
