class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited=set({})
        def play(matrix, x, y):
            if matrix[x][y]=='M':
                matrix[x][y]='X'
                return
            elif matrix[x][y]=='E':
                # check if any mines are adjacent to it
                mine=0
                for dirx, diry in pairwise([-1,0,1,0,-1,-1,1,1,-1]):
                    if 0<=x+dirx<len(matrix) and 0<=y+diry<len(matrix[0]):
                        if matrix[x+dirx][y+diry]=='M':
                            mine+=1
                if mine!=0:
                    matrix[x][y]=str(mine)
                else:
                    matrix[x][y]='B'
                    visited.add((x, y))
                    # recursively
                    for dirx, diry in pairwise([-1,0,1,0,-1,-1,1,1,-1]):
                        if 0<=x+dirx<len(matrix) and 0<=y+diry<len(matrix[0]) and (x+dirx, y+diry) not in visited:
                            visited.add((x+dirx, y+diry))
                            play(board, x+dirx, y+diry)
        play(board, click[0], click[1])
        return board