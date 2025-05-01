class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # use union find
        # if the queries have same parents return True
        parent=list(range(n))
        rank=[1]*n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return True
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
        def find(n):
            while n!=parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        # only look at pairwise to group
        for (i, n), (j, m) in pairwise(enumerate(nums)):
            if abs(n-m)<=maxDiff:
                union(i, j)
        return [find(u)==find(v) for u, v in queries]
        