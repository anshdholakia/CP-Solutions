class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked=set({})
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        total=0
        while heap:
            while heap and heap[0][1] in marked:
                heapq.heappop(heap)
            if heap:
                val, idx = heapq.heappop(heap)
                total+=val
                marked.add(idx-1)
                marked.add(idx+1)
        return total