class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # use a heap to greedily take the events here
        minheap=[]
        res=0
        current_day=0
        idx=0
        events.sort(key=lambda x:x[0])
        while minheap or idx<len(events):
            if not minheap:
                current_day=events[idx][0]
            # add events to heap till it satisfies
            while idx<len(events) and events[idx][0]==current_day:
                heapq.heappush(minheap, events[idx][1])
                idx+=1
            heapq.heappop(minheap)
            res+=1
            current_day+=1
            # remove stale events
            while minheap and minheap[0]<current_day:
                heapq.heappop(minheap)
        return res


