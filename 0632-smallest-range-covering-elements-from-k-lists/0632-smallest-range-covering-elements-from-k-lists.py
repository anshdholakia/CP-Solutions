class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k=[0]*len(nums)
        left, right = min([n[0] for n in nums]), max([n[0] for n in nums])
        minheap=[(n[0], i, 0) for i,n in enumerate(nums)]
        heapq.heapify(minheap)
        res_left, res_right = -float("inf"), float("inf")
        while True:
            mv_val, mv_idx, mv_list_idx=heapq.heappop(minheap)
            if (right-left)<(res_right-res_left):
                res_left, res_right=left, right
            if mv_list_idx+1==len(nums[mv_idx]):
                return [res_left, res_right]
            heapq.heappush(minheap, (nums[mv_idx][mv_list_idx+1], mv_idx, mv_list_idx+1))
            right=max(right, nums[mv_idx][mv_list_idx+1])
            left=minheap[0][0]