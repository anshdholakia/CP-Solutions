class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # boil this question down to 2 lists
        # always shift the smallest list element pointer here
        right = -inf
        minheap=[]
        for i in range(len(nums)):
            heapq.heappush(minheap, (nums[i][0], nums[i], 0)) # val, list no, pointer pos
            right=max(right, nums[i][0])
        left=minheap[0][0]
        final_left, final_right = left, right
        while True:
            val, l, ptr = heapq.heappop(minheap)
            if ptr==len(l)-1:
                break
            ptr+=1
            heapq.heappush(minheap, (l[ptr], l, ptr))
            right=max(right, l[ptr])
            left=minheap[0][0]
            if right-left<final_right-final_left:
                final_left, final_right = left, right
        return final_left, final_right
