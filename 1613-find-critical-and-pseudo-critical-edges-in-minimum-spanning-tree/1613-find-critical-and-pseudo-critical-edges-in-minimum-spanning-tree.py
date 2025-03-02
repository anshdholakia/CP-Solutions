class UnionFind:
    def __init__(self, n):
        self.parent=list(range(n))
        self.rank=[1]*n
    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.parent[p2]=p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.parent[p1]=p2
        return True
    def find(self, n):
        while n!=self.parent[n]:
            self.parent[n]=self.parent[self.parent[n]]
            n=self.parent[n]
        return n
    def reset(self, n):
        self.__init__(n)

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # use kruskal to union find the mst
        # traverse throught each edge and check if mst can be made without it
        # if the weight of new mst is more than optimal, its critical
        # if the weight of the new mst if equal and including it again makes the new mst, its pseudo
        # else we can ignore the edge
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x: x[2])
        uf=UnionFind(n)
        mst_val=0
        for n1, n2, w, _ in edges:
            if uf.union(n1, n2):
                mst_val+=w
        critical, pseudo = [], []
        for m1, m2, e_w, i in edges:
            # check if you can make mst without it
            new_mst=0
            uf.reset(n)
            for n1, n2, w, j in edges:
                if i!=j and uf.union(n1, n2):
                    new_mst+=w
            if max(uf.rank)!=n or new_mst>mst_val:
                critical.append(i)
                continue
            # check if you can make mst with it for validating
            # its part of the original mst
            uf.reset(n)
            uf.union(m1, m2)
            new_mst=e_w
            for n1, n2, w, j in edges:
                if i!=j and uf.union(n1, n2):
                    new_mst+=w
            if new_mst==mst_val:
                pseudo.append(i)
        return critical, pseudo
