class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # find all nodes which make a cycle
        G=defaultdict(list)
        for i in range(len(graph)):
            for n in graph[i]:
                G[i].append(n)
        cycle=set({})
        visited=set({})
        def topo(c):
            # returns if this makes a cycle or not
            if c in visited:
                return True
            if c in cycle:
                return False
            cycle.add(c)
            for n in G[c]:
                if not topo(n):
                    return False
            cycle.remove(c)
            visited.add(c)
            return True
        res=[]
        for i in range(len(graph)):
            if topo(i):
                res.append(i)
        return res