from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols, ldiag, rdiag = set({}), set({}), set({})
        def backtrack(row):
            if row==n:
                result.append(["".join(x) for x in board])
            for c in range(n):
                if c not in cols and c+row not in rdiag and c-row not in ldiag:
                    cols.add(c)
                    rdiag.add(c+row)
                    ldiag.add(c-row)
                    board[row][c] = 'Q'
                    backtrack(row+1)
                    board[row][c] = '.'
                    cols.remove(c)
                    rdiag.remove(c+row)
                    ldiag.remove(c-row)
                    


        backtrack(0)
        return result