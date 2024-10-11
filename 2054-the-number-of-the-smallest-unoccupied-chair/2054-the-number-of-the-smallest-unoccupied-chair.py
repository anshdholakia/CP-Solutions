from sortedcontainers import SortedSet
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        ss = SortedSet()
        ti = sorted(list(enumerate(times)), key=lambda x: x[1])
        visited = {}
        minheap = []
        min_chair = 0
        for i, t in ti:
            while minheap and t[0]>=minheap[0][0]:
                j = heapq.heappop(minheap)[1]
                ss.add(visited[j])
                min_chair = min(min_chair, visited[j])
                del visited[j]
            heapq.heappush(minheap, (t[1], i))
            if not ss:
                min_chair = len(visited)
            else:
                min_chair = ss[0]
                ss.discard(min_chair)
            visited[i] = min_chair
            if i==targetFriend:
                break
        return min_chair


        