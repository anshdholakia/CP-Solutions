class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        G=defaultdict(list)
        for u, v in prerequisites:
            G[u].append(v)
        cycle=set({})
        visited=set({})
        def dfs(n):
            if n in visited:
                return True
            if n in cycle:
                return False
            cycle.add(n)
            for neighbor in G[n]:
                if not dfs(neighbor):
                    return False
            cycle.remove(n)
            visited.add(n)
            res.append(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res