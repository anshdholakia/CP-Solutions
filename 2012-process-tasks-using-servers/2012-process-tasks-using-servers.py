class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        minheap=[(s, i) for i, s in enumerate(servers)]
        heapq.heapify(minheap)
        res=[]
        queue=[]
        time=0
        idx=0
        while idx<len(tasks):
            time=max(time, idx) # important
            if not minheap:
                time=queue[0][0]
            while queue and queue[0][0]<=time:
                pop=heapq.heappop(queue)
                heapq.heappush(minheap, pop[1:])
            pops, popi = heapq.heappop(minheap)
            res.append(popi)
            heapq.heappush(queue, (time+tasks[idx], pops, popi))
            idx+=1
        return res