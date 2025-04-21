class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=collections.Counter(tasks)
        waiting=collections.deque()
        maxheap=[-v for _, v in count.items()]
        heapq.heapify(maxheap)
        time=0
        while maxheap or waiting:
            while waiting and waiting[0][0]<=time:
                heapq.heappush(maxheap, waiting.popleft()[1])
            if maxheap:
                pop=heapq.heappop(maxheap)
                if pop+1:
                    waiting.append((time+n+1, pop+1))
                time+=1
            else:
                time=waiting[0][0]
        return time