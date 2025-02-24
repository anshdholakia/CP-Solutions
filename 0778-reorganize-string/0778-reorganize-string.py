class Solution:
    def reorganizeString(self, s: str) -> str:
        # scheduling task with k=1
        count=collections.Counter(s)
        heap=[(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        queue=collections.deque([])
        time=0
        res=""
        while heap or queue:
            while queue and queue[0][0]<=time:
                heapq.heappush(heap, queue.popleft()[1:3])
            if heap:
                val, key = heapq.heappop(heap)
                res+=key
                if val+1!=0:
                    queue.append((time+2, val+1, key))
            else:
                return ""
            time+=1
        return res
