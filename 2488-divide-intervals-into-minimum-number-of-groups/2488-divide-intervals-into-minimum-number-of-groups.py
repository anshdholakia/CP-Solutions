class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minheap = []
        for s, e in intervals:
            if minheap and minheap[0]<s:
                heapq.heappop(minheap)
            heapq.heappush(minheap, e)
        return len(minheap)