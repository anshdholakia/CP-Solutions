class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # multi source bfs
        queue = collections.deque([])
        visited=set({})
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in pairwise([-1,0,1,0,-1]):
                    if 0<=dx+x<len(mat) and 0<=dy+y<len(mat[0]) and (dx+x, dy+y) not in visited and mat[dx+x][dy+y]==1:
                        visited.add((dx+x, dy+y))
                        mat[dx+x][dy+y]=mat[x][y]+1
                        queue.append((dx+x, dy+y))
        return mat
