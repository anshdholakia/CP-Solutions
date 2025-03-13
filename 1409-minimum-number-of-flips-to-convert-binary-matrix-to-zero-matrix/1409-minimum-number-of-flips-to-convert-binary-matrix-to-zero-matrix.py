class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        level=0
        queue=collections.deque([mat])
        visited=set({tuple(map(tuple, mat))})
        while queue:
            for _ in range(len(queue)):
                pop=queue.popleft()
                if sum(map(sum, pop))==0:
                    return level
                for i in range(len(pop)):
                    for j in range(len(pop[0])):
                        new_mat=self.flip(pop, i, j)
                        hash_mat=tuple(map(tuple, new_mat))
                        if hash_mat not in visited:
                            visited.add(hash_mat)
                            queue.append(new_mat)
            level+=1
        return -1
    def flip(self, matrix, x, y):
        res=deepcopy(matrix)
        res[x][y]^=1
        for dirx, diry in pairwise([-1,0,1,0,-1]):
            if 0<=x+dirx<len(matrix) and 0<=y+diry<len(matrix[0]):
                res[x+dirx][y+diry]^=1
        return res