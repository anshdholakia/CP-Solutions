class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals=[(i-r, i+r) for i, r in enumerate(ranges)]
        intervals.sort()
        idx=0
        maxheap=[]
        dist=0
        res=0
        while idx<len(intervals) or maxheap:
            while idx<len(intervals) and intervals[idx][0]<=dist:
                heapq.heappush(maxheap, -intervals[idx][1])
                idx+=1
            if not maxheap or dist>-maxheap[0]: 
                return -1
            dist=-heapq.heappop(maxheap)
            res+=1
            if dist>=n: break
        return res