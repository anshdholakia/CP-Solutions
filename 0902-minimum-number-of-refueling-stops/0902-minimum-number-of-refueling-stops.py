class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # use a heap
        # this is like the bricks and ladders problem
        # if u empty your fuel
        # check the stations you went past and select the max fuel station
        cur=0
        heapq.heapify(stations)
        distance=startFuel
        res=0
        maxheap=[]
        while distance<target:
            while stations and stations[0][0]<=distance:
                heapq.heappush(maxheap, -heapq.heappop(stations)[1])
            if maxheap:
                distance-=heapq.heappop(maxheap)
            else:
                return -1
            res+=1
        return res