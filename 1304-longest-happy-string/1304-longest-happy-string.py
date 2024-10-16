class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(maxheap)
        queue = collections.deque([])
        cur_t = 0
        result = ""
        while maxheap:
            popv, popc = heapq.heappop(maxheap)
            if result and result[-2:]==popc*2:
                queue.append((popv, popc))
                continue
            result += popc*min(-popv, 1)
            # append to queue
            popv+=min(-popv, 1)
            if queue:
                heapq.heappush(maxheap, queue.popleft())
            if popv:
                heapq.heappush(maxheap, (popv, popc))
        return result