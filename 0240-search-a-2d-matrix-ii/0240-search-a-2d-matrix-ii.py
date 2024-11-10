class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            idx=bisect_left(r, target)
            if 0<=idx<len(r) and r[idx]==target:
                return True
        return False