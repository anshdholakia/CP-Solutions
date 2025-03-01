class Solution:
    def totalNQueens(self, n: int) -> int:
        # backtracking to add to global result
        result=0
        cols, ldiag, rdiag = set({}), set({}), set({})
        def backtrack(row):
            if row==n:
                nonlocal result
                result+=1
                return
            for col in range(n):
                if col+row not in ldiag and col-row not in rdiag and col not in cols:
                    cols.add(col)
                    ldiag.add(col+row)
                    rdiag.add(col-row)
                    backtrack(row+1)
                    cols.remove(col)
                    ldiag.remove(col+row)
                    rdiag.remove(col-row)

        backtrack(0)
        return result