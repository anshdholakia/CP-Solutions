class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s=[x[0] for x in intervals]
        e=[x[1] for x in intervals]
        s.sort()
        e.sort()
        i, j = 0, 0
        res=1
        cnt=0
        while i<len(s) and j<len(e):
            if e[j]<=s[i]:
                j+=1
                cnt-=1
            else:
                cnt+=1
                i+=1
            res=max(res, cnt)
        return res