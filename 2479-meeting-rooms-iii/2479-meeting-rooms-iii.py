class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms=list(range(n))
        frequency=defaultdict(int)
        in_use=[]
        meetings.sort(key=lambda x:x[0])
        idx=0
        while idx<len(meetings):
            s, e = meetings[idx]
            while in_use and in_use[0][0]<=s:
                heapq.heappush(available_rooms, heapq.heappop(in_use)[1])
            if available_rooms:
                room=heapq.heappop(available_rooms)
                heapq.heappush(in_use, (e, room))
            else:
                latest, room = heapq.heappop(in_use)
                delay=latest-s
                heapq.heappush(in_use, (e+delay, room))
            frequency[room]+=1
            idx+=1
        res=None
        for k in sorted(frequency.keys()):
            if res==None or frequency[k]>frequency[res]:
                res=k
        return res
            