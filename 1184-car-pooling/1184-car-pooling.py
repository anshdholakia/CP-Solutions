class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        idx=0
        trips.sort(key=lambda x:x[1])
        heap=[]
        cur_cap=0
        while idx<len(trips):
            while heap and heap[0][0]<=trips[idx][1]:
                cur_cap-=heapq.heappop(heap)[1]
            cur_cap+=trips[idx][0]
            heapq.heappush(heap, (trips[idx][2], trips[idx][0]))
            if cur_cap>capacity:
                return False
            idx+=1
        return True