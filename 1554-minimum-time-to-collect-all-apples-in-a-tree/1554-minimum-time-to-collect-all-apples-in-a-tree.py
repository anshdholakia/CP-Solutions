class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G=defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        # recursive call to get true of false
        visited=set({0})
        def dfs(node):
            apple=hasApple[node]
            sum_dist=0
            for n in G[node]:
                if n not in visited:
                    visited.add(n)
                    rec_apple, distance = dfs(n)
                    sum_dist+=distance
                    apple = apple or rec_apple
            if apple:
                # this means this path leads to an apple
                return apple, 1+sum_dist
            return apple, 0
        result=dfs(0)
        return max(0, 2*(result[1]-1))
