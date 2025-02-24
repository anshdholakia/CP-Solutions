class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[(t[0], t[1], i) for i, t in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0])
        heap=[]
        time=tasks[0][0]
        res=[]
        idx=0
        while heap or idx<len(tasks):
            while idx<len(tasks) and tasks[idx][0]<=time:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx+=1
            if heap:
                inc, id = heapq.heappop(heap)
                res.append(id)
                time+=inc
            elif idx<len(tasks):
                time=tasks[idx][0]
        return res