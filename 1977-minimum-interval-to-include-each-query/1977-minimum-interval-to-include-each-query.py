class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        orig_queries=queries.copy()
        queries=list(set(queries))
        queries.sort()
        minheap=[]
        memo={}
        idx=0
        for q in queries:
            # add the intervals to the heap
            while idx<len(intervals) and intervals[idx][0]<=q:
                heapq.heappush(minheap, (intervals[idx][1]-intervals[idx][0]+1, intervals[idx][1]))
                idx+=1
            # remove any stale values in heap
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            memo[q]=minheap[0][0] if minheap else -1
        return [memo[q] for q in orig_queries]
