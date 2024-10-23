from sortedcontainers import SortedList
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        G = defaultdict(lambda: SortedList())
        for fro, to in tickets:
            G[fro].add(to)
        visited=[]
        def dfs(airport):
            if len(visited)==len(tickets):
                visited.append(airport)
                return True
            for n in G[airport]:
                visited.append(airport)
                G[airport].remove(n)
                if dfs(n):
                    return visited
                G[airport].add(n)
                visited.pop()
        return dfs("JFK")