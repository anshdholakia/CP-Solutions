class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        G=defaultdict(list)
        rank=[1]*len(edges)
        parent=list(range(len(edges)))
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]] # path compression
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
        for a, b in edges:
            if not union(a-1, b-1):
                return (a, b)