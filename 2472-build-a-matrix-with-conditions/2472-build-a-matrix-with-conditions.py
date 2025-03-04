class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        result=[[0]*k for _ in range(k)]
        G_row=defaultdict(list)
        G_col=defaultdict(list)
        for above, below in rowConditions:
            G_row[above].append(below)
        for left, right in colConditions:
            G_col[left].append(right)
        # find topo of row
        row_topo=[]
        cycle=set({})
        visited=set({})
        def dfs(n, topo, graph):
            if n in cycle:
                return False
            if n in visited:
                return True
            cycle.add(n)
            for nei in graph[n]:
                if not dfs(nei, topo, graph):
                    return False
            cycle.remove(n)
            visited.add(n)
            topo.append(n)
            return True
        
        for i in range(1, k+1):
            if not dfs(i, row_topo, G_row):
                return []
        
        row_topo={x: i for i, x in enumerate(reversed(row_topo))}
        print(row_topo)

        col_topo=[]
        visited=set({})
        for i in range(1, k+1):
            if not dfs(i, col_topo, G_col):
                return []
        col_topo={x: i for i, x in enumerate(reversed(col_topo))}
        for i in range(1, k+1):
            result[row_topo[i]][col_topo[i]]=i
        return result