class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=list(map(lambda x:-x, gifts))
        heapq.heapify(gifts)
        for _ in range(k):
            heapq.heappush(gifts, -floor(sqrt(-heapq.heappop(gifts))))
        return sum(list(map(lambda x:-x,gifts)))