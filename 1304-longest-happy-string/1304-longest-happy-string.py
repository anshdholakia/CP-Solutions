class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # time scheduling problem
        res=""
        minheap=[(-a,'a',0), (-b,'b',0), (-c,'c',0)] # count, char, count used in row
        minheap=[x for x in minheap if x[0]!=0]
        heapq.heapify(minheap)
        queue=collections.deque([])
        time=0
        while minheap or queue:
            if queue and queue[0][0]==time:
                heapq.heappush(minheap, queue.popleft()[1:])
            if minheap:
                val, char, used = heapq.heappop(minheap)
                res+=char
                used+=1
                if used%2==0 and (val+1)!=0:
                    queue.append((time+2, val+1, char, 0))
                elif (val+1)!=0:
                    heapq.heappush(minheap, (val+1, char, used))
            else:
                break
            time+=1
        return res