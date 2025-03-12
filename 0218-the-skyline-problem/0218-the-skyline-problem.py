class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap=[]
        result=[]
        events=[]
        # split the start and end 
        for s, e, h in buildings:
            events.append((s, -1, h))
            events.append((e, 1, h))
        events.sort(key=lambda x: (x[0], x[1], x[1]*x[2]))
        freq=defaultdict(int) # keep the frequency of the height
        for t, op, height in events:
            if op==-1:
                heapq.heappush(heap, -height)
                freq[height]+=1
            elif op==1:
                freq[height]-=1
                while heap and freq[-heap[0]]==0:
                    heapq.heappop(heap)
            if not result or (result[-1][1]!=-heap[0] if heap else result[-1][1]!=0):
                result.append((t, -heap[0] if heap else 0))
        return result