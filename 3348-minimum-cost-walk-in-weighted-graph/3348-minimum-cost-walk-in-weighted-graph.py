class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        group_minimum={}
        # in a bitwise and, once you reach a minimum no matter where you traverse
        # you will still have the minimum value
        # find the groups and find minimum in each edge
        parent=list(range(n))
        rank=[1]*n
        def union(a, b, w):
            p1, p2 = find(a), find(b)
            if p1 in group_minimum:
                w&=group_minimum[p1]
            if p2 in group_minimum:
                w&=group_minimum[p2]
            if p1==p2:
                group_minimum[p1]=w
                group_minimum[p2]=w
                return
            if rank[p1]<rank[p2]:
                rank[p2]+=rank[p1]
                parent[p1]=p2
                group_minimum[p2]=w
            else:
                rank[p1]+=rank[p2]
                parent[p2]=p1
                group_minimum[p1]=w
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        G=defaultdict(list)
        for u, v, w in edges:
            union(u, v, w)
        result=[]
        for u, v in query:
            p1, p2 = find(u), find(v)
            if p1!=p2: 
                result.append(-1)
                continue
            result.append(group_minimum[p1])
        return result
        
        

