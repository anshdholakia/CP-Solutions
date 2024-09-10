class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        # keep the one with the smallest end time if colliding
        stack = []
        result = 0
        for s, e in intervals:
            if stack and stack[-1][1]>s:
                # keep the one with the smallest end time
                popped = stack.pop()
                if popped[-1]<e:
                    s, e = popped
                result+=1
            stack.append((s, e))
        return result
