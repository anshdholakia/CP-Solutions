class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        start, end = [m[0] for m in meetings], [m[1] for m in meetings]
        start.sort()
        end.sort()
        s, e = 0, 0
        result=start[0]-1
        cur_day=start[0]
        while s<len(start) and e<len(end):
            if end[e]<start[s]:
                cur_day=end[e]+1
                e+=1 
            elif start[s]<=end[e]:
                s+=1
            if s==e:
                result+=(start[s]-cur_day)
        return result+(days-end[-1])