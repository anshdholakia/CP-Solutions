class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        heap=[]
        res=-inf
        for i in range(len(values)):
            if heap:
                res=max(res, -heap[0]+values[i]-i)
            heapq.heappush(heap, -values[i]-i)
        return res