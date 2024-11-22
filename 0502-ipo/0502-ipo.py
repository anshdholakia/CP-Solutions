class Solution:
    def findMaximizedCapital(self, k: int, w: int, profit: List[int], capital: List[int]) -> int:
        sorted_investments=sorted([(c, p) for p, c in zip(profit, capital)], key=lambda x:(x[0], x[1]))
        maxheap=[]
        idx=-1
        cur_cap=w
        for _ in range(k):
            for i in range(idx+1, len(sorted_investments)):
                if sorted_investments[i][0]>cur_cap:
                    break
                idx=i
                heapq.heappush(maxheap, -sorted_investments[i][1])
            if not maxheap:
                continue
            cur_cap-=heapq.heappop(maxheap)
        return cur_cap