class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = set({}), set({})
        ignore_rows, ignore_cols = set({}), set({})
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=='B':
                    if i in rows or j in cols:
                        ignore_rows.add(i)
                        ignore_cols.add(j)
                    rows.add(i)
                    cols.add(j)
        valid_rows = rows-ignore_rows
        valid_cols = cols-ignore_cols
        result = 0
        for row in valid_rows:
            for col in valid_cols:
                if picture[row][col]=='B':
                    result+=1
        return result