class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # simple heap solutions
        intervals=[[s, e, p] for s, e, p in zip(startTime, endTime, profit)]
        intervals.sort(key=lambda x: x[0])
        result=0
        heap=[]
        idx=0
        max_last=0
        while idx<len(intervals):
            min_time=intervals[idx][0]
            # get the max_last popped from the heap
            while heap and heap[0][0]<=min_time:
                max_last=max(max_last, heapq.heappop(heap)[1])
            while idx<len(intervals) and intervals[idx][0]==min_time:
                result=max(result, max_last+intervals[idx][2])
                heapq.heappush(heap, (intervals[idx][1], max_last+intervals[idx][2]))
                idx+=1
        return result
                
