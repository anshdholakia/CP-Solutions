class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set({})
        def backtrack(x, y, idx):
            if idx==len(word):
                return True
            if board[x][y]!=word[idx]:
                return False
            visited.add((x, y))
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+x<len(board) and 0<=dy+y<len(board[0]) and (dx+x,dy+y) not in visited:
                    if backtrack(dx+x, dy+y, idx+1):
                        return True
            visited.remove((x,y))
            return idx==len(word)-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False