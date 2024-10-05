class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            curr=points[i]
            if curr[0]<=prev[1]:
                count-=1
                prev = [curr[0], min(curr[1], prev[1])]
                continue
            prev=curr
        return count
            