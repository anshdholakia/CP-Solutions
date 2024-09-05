class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for s, e in intervals:
            if stack and stack[-1][-1]>=s:
                s = min(stack[-1][0], s)
                e = max(stack[-1][1], e)
                stack.pop()
            stack.append([s, e])
        return stack


            