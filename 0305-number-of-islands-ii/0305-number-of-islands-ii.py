class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans=[]
        # union find algo
        graph = [[0]*n for _ in range(m)]
        parents=set({})
        parent, rank = {(i, j): (i, j) for i in range(m) for j in range(n)}, defaultdict(lambda: 1)
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        def union(a, b):
            p1, p2 = find(a), find(b)
            while p1==p2:
                return
            if rank[p1]>=rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
                if p2 in parents:
                    parents.remove(p2)
                parents.add(p1)
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
                if p1 in parents:
                    parents.remove(p1)
                parents.add(p2)
        for u, v in positions:
            if graph[u][v]:
                ans.append(len(parents))
                continue
            parents.add((u, v))
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=u+dx<m and 0<=v+dy<n and graph[u+dx][v+dy]:
                    union((u, v), (u+dx, v+dy))
                graph[u][v]=1
            ans.append(len(parents))
        return ans