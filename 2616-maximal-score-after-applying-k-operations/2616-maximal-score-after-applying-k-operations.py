class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        minheap = [-x for x in nums]
        heapq.heapify(minheap)
        for _ in range(k):
            val=heapq.heappop(minheap)
            score+=-val
            heapq.heappush(minheap, -ceil(-val/3.0))
        return score