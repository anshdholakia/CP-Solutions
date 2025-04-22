class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # use prims
        edges=[]
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                x, y = points[p1]
                p, q = points[p2]
                edges.append((abs(x-p)+abs(y-q), p1, p2))
        edges.sort(key=lambda x: x[0])
        parent=list(range(len(points)))
        rank=[1]*len(points)
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        res=0
        for d, u, v in edges:
            if union(u, v):
                res+=d
        return res