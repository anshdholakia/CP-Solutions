class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        power = [1]*len(edges)
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return False
            if power[p1]>=power[p2]:
                par[p2]=p1
                power[p1]+=power[p2]
            else:
                par[p1]=p2
                power[p2]+=power[p1]
            return True
        def find(n):
            while n!=par[n]:
                n=par[n]
                par[n]=par[par[n]]
            return n
        for a, b in edges:
            if not union(a-1, b-1):
                return [a, b]
