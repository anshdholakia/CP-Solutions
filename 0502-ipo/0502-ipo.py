class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # we would like to minimize the capital req
        # but maximize the profit
        # since we aren't going to subtract from profit
        # our current capital is always increasing
        pc=[(c, p) for p, c in zip(profits, capital)]
        pc.sort(key=lambda x: x[0])
        idx=0
        heap=[]
        cur_k=0
        while idx<len(pc) or heap:
            while idx<len(pc) and pc[idx][0]<=w:
                heapq.heappush(heap, -pc[idx][1])
                idx+=1
            if heap:
                w-=heapq.heappop(heap)
                cur_k+=1
                if cur_k==k: break
            else:
                break
        return w
