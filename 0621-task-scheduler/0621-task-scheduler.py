class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = collections.deque([])
        cur_time = 0
        minheap = [-v for v in collections.Counter(tasks).values()]
        heapq.heapify(minheap)
        while minheap or queue:
            cur_time+=1
            if minheap:
                pop = heapq.heappop(minheap)
                pop+=1
                if pop:
                    queue.append((cur_time+n, pop))
            if queue and queue[0][0]<=cur_time:
                _, pop = queue.popleft()
                heapq.heappush(minheap, pop)
        return cur_time