class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort the logs using the ts
        logs.sort(key=lambda x: x[0])
        # using union find find if everyone is in one group
        parents, ranks = list(range(n)), [1]*n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return p1
            if ranks[p1]>ranks[p2]:
                parents[p2]=p1
                ranks[p1]+=ranks[p2]
                return p1
            else:
                parents[p1]=p2
                ranks[p2]+=ranks[p1]
                return p2
        def find(n):
            while n!=parents[n]:
                parents[n]=parents[parents[n]] # path compression
                n=parents[n]
            return n
        for ts, a, b in logs:
            if ranks[union(a, b)]==n:
                return ts
        return -1