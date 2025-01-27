class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        G = defaultdict(list)
        for fromm, to in prerequisites:
            G[fromm].append(to)
        nodeToChildren=defaultdict(set) # node value: set of children
        # nodeToChildren={1: set(0, 2), 2: set(0), 0: set()}
        # BFS on EACH NODE
        def bfs(node):
            queue=collections.deque([node])
            visited=set({})
            while queue:
                pop=queue.popleft()
                for neighbor in G[pop]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        if nodeToChildren[neighbor]:
                            visited.update(nodeToChildren[neighbor])
                        else:
                            queue.append(neighbor)
            nodeToChildren[node].update(visited)
        for i in range(numCourses):
            bfs(i)
        res=[]
        for a, b in queries:
            if b in nodeToChildren[a]:
                res.append(True)
            else:
                res.append(False)
        return res