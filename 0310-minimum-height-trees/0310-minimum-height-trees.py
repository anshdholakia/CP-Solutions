class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        G=defaultdict(set)
        for a, b in edges:
            G[a].add(b)
            G[b].add(a)
        leaves=[]
        edge_count=defaultdict(int)
        for k, v in G.items():
            if len(v)==1:
                leaves.append(k)
            edge_count[k]=len(v)
        new_leaves=[]
        while True:
            for node in leaves:
                for neigh in G[node]:
                    # you cannot simply add this to leaves since the edge count is still more than 1
                    edge_count[neigh]-=1
                    if edge_count[neigh]==1:
                        new_leaves.append(neigh)
            if not new_leaves:
                break
            leaves=new_leaves.copy()
            new_leaves=[]
        return leaves