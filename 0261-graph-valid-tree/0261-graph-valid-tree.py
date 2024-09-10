class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        power = [1]*n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return False
            if power[p1]>power[p2]:
                parent[p2]=p1
                power[p1]+=power[p2]
            else:
                parent[p1]=p2
                power[p2]+=power[p1]
            return True
        def find(a):
            while a!=parent[a]:
                a=parent[parent[a]]
            return a
        for a, b in edges:
            if not union(a, b):
                return False
        return max(power)==n