class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result=[-1]*len(queries)
        intervals.sort()
        queries=list(enumerate(queries))
        queries.sort(key=lambda x: x[1])
        minheap=[]
        idx=0
        for i, q in queries:
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            while idx<len(intervals):
                if intervals[idx][0]<=q<=intervals[idx][1]:
                    heapq.heappush(minheap, (intervals[idx][1]-intervals[idx][0]+1, intervals[idx][1]))
                elif q<=intervals[idx][1]:
                    break
                idx+=1
            result[i]=minheap[0][0] if minheap else -1
        return result
            