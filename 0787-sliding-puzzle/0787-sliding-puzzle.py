class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # use bfs
        def hash_board(board):
            return tuple([tuple(row) for row in board])
        sx, sy = None, None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==0:
                    sx, sy = i, j
        final_state=hash_board([[1, 2, 3], [4, 5, 0]])
        visited=set({hash_board(board)})
        queue=collections.deque([(board, sx, sy)])
        level=-1
        while queue:
            level+=1
            for _ in range(len(queue)):
                pop_board, x, y=queue.popleft()
                if hash_board(pop_board)==final_state:
                    return level
                for dx, dy in pairwise([-1,0,1,0,-1]):
                    if 0<=x+dx<len(board) and 0<=y+dy<len(board[0]):
                        pop_board[x][y], pop_board[x+dx][y+dy]=pop_board[x+dx][y+dy], pop_board[x][y]
                        hash_val=hash_board(pop_board)
                        if hash_val not in visited:
                            visited.add(hash_val)
                            queue.append((deepcopy(pop_board), dx+x, dy+y))
                        pop_board[x][y], pop_board[x+dx][y+dy]=pop_board[x+dx][y+dy], pop_board[x][y]
        return -1
