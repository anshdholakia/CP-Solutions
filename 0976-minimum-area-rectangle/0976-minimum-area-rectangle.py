class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result=inf
        point_set=set([tuple(x) for x in points])
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x, y = points[i]
                p, q = points[j]
                if x==p or q==y:
                    continue
                if (x, q) in point_set and (p, y) in point_set:
                    result=min(result, abs(x-p)*abs(q-y))
        return result if result!=inf else 0