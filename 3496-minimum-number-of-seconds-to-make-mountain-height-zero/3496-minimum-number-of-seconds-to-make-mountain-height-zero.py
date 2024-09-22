class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        options = [(x, 1, x) for x in workerTimes] # these are the options we have to cut 1 inch
        heapq.heapify(options)
        res = 0
        while mountainHeight:
            mountainHeight-=1
            x, y, z = heapq.heappop(options)
            res = x
            heapq.heappush(options, (x+(z*(y+1)), y+1, z))
        return res