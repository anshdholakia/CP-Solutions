class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k_ptrs = [0]*len(nums)
        lower, upper = min([n[0] for n in nums]), max([n[0] for n in nums])
        res = [lower, upper]
        minheap = [(n[0], i, 0) for i, n in enumerate(nums)]
        heapq.heapify(minheap)
        while True:
            # pop the element to move
            val, list_idx, elem_idx = heapq.heappop(minheap)
            elem_idx +=1
            if elem_idx==len(nums[list_idx]):
                break
            next_val = nums[list_idx][elem_idx]
            heapq.heappush(minheap, (next_val, list_idx, elem_idx))
            lower = minheap[0][0]
            upper = max(upper, next_val)
            if upper-lower<res[1]-res[0]:
                res=[lower, upper]
        return res


