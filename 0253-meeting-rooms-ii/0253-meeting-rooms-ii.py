class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        i, k = 0, 0
        result = 0
        cur_count = 0
        while i<len(start) and k<len(end):
            if end[k]<=start[i]:
                cur_count-=1
                k+=1
            elif start[i]<end[k]:
                cur_count+=1
                i+=1
            result = max(result, cur_count)
        return result
