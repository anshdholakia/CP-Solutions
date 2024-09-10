class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        max_end = float("-inf")
        for s, e in intervals:
            if s<max_end:
                return False
            max_end = max(e, max_end)
        return True