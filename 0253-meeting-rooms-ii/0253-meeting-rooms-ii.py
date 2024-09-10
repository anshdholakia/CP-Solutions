class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s = [s for s, e in sorted(intervals)]
        e = [e for s, e in sorted(intervals, key=lambda x: x[1])]
        p1, p2 = 0, 0
        result, cur_count = 0, 0
        while p1<len(s) and p2<len(e):
            if s[p1]<e[p2]:
                cur_count+=1
                p1+=1
            else:
                cur_count-=1
                p2+=1
            result=max(result, cur_count)
        return result
        