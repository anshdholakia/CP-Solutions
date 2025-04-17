class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=[['.']*n for _ in range(n)]
        ldiag, rdiag, column = set({}), set({}), set({})
        def backtrack(row):
            if row==n:
                result.append(["".join(x) for x in board])
                return
            for col in range(n):
                if row+col not in ldiag and row-col not in rdiag and col not in column:
                    column.add(col)
                    ldiag.add(row+col)
                    rdiag.add(row-col)
                    board[row][col]='Q'
                    backtrack(row+1)
                    board[row][col]='.'
                    column.remove(col)
                    ldiag.remove(row+col)
                    rdiag.remove(row-col)
        backtrack(0)
        return result