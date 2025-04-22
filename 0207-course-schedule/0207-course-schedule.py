class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G=defaultdict(list)
        for u, v in prerequisites:
            G[u].append(v)
        cycle=set({})
        def dfs(n):
            if not G[n]:
                return True
            if n in cycle:
                return False
            cycle.add(n)
            for neighbor in G[n]:
                if not dfs(neighbor):
                    return False
            cycle.remove(n)
            G[n]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
