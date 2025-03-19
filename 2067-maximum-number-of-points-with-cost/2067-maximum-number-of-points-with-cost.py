class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # this is a dp problem
        # for each of the row tho, traverse from left side and right side
        # take the max of the element on top and element to the left and right
        prev_row=0
        row=0
        for row in range(1, len(points)):
            left, right = [0]*len(points[0]), [0]*len(points[0])
            left[0]=points[prev_row][0]
            for c in range(1, len(points[0])):
                left[c]=max(left[c-1]-1, points[row-1][c])
            right[-1]=points[prev_row][-1]
            for c in range(len(points[0])-2, -1, -1):
                right[c]=max(right[c+1]-1, points[row-1][c])
            for c in range(len(points[0])):
                points[row][c]+=max(left[c], right[c])
            prev_row=row
        return max(points[row])