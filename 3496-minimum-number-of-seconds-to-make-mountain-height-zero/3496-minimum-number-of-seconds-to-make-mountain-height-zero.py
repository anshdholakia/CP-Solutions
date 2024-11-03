class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        minheap=[(w, 1, w) for w in workerTimes]
        heapq.heapify(minheap)
        res=0
        for _ in range(mountainHeight):
            x,y,z=heapq.heappop(minheap)
            res=max(res, x)
            heapq.heappush(minheap, (x+z*(y+1), y+1, z))
        return res
            
