class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # union find
        par=[i for i in range(len(isConnected))]
        power=[1]*len(isConnected)
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1==p2:
                return False
            if power[p1]>power[p2]:
                power[p1]+=power[p2]
                par[p2]=p1
            else:
                power[p2]+=power[p1]
                par[p1]=p2
            return True
        def find(n):
            while n!=par[n]:
                par[n]=par[par[n]] # path compression
                n=par[n]
            return n
        res=len(isConnected)
        for n1 in range(len(isConnected)):
            for n2 in range(len(isConnected[n1])):
                if n1!=n2 and isConnected[n1][n2]:
                    if union(n1, n2):
                        res-=1
        return res