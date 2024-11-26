class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        G=defaultdict(list)
        for u, v in edges:
            G[v].append(u)
        res=[x for x in range(n) if not G[x]]
        return res[0] if len(res)==1 else -1