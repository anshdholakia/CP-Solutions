class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        for p, c in prerequisites:
            G[p].append(c)

        cycle = set({})
        visited = set({})
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            visited.add(course)
            cycle.add(course)
            for neighbor in G[course]:
                if not dfs(neighbor):
                    return False
            cycle.remove(course)
            return True
        for c in range(numCourses):
            if c not in visited and not dfs(c):
                return False
        return True