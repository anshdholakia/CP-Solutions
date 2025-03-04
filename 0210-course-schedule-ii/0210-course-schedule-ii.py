class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G=defaultdict(list)
        for fro, to in prerequisites:
            G[fro].append(to)
        res=[]
        cycle=set({})
        visited=set({})
        def dfs(n):
            if n in cycle:
                return False
            if n in visited:
                return True
            visited.add(n)
            if not G[n]:
                res.append(n)
                return True
            cycle.add(n)
            for neigh in G[n]:
                if not dfs(neigh):
                    return False
            cycle.remove(n)
            G[n].clear()
            res.append(n)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res