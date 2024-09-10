class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for p, c in prerequisites:
            G[c].append(p)

        topo = []
        cycle = set({})
        visited = set({})
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            visited.add(course)
            if not G[course]:
                topo.append(course)
                return True
            cycle.add(course)
            for n in G[course]:
                if not dfs(n):
                    return False
            cycle.remove(course)
            topo.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return topo[::-1]