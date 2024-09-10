class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected_cmp = set({})
        parent = [i for i in range(n)]
        power = [1]*n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return
            if power[p1]>=power[p2]:
                if p2 in connected_cmp:
                    connected_cmp.remove(p2)
                connected_cmp.add(p1)
                parent[p2]=p1
                power[p1]+=power[p2]
            else:
                if p1 in connected_cmp:
                    connected_cmp.remove(p1)
                connected_cmp.add(p2)
                parent[p1]=p2
                power[p2]+=power[p1]
        def find(a):
            while a!=parent[a]:
                a=parent[parent[a]]
            return a
        for a, b in edges:
            union(a, b)
        # last check to find single nodes
        additional = 0
        for i in range(n):
            if power[i]==1 and parent[i]==i:
                additional+=1
        return len(connected_cmp)+additional