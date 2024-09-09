# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        left, right = 0, n-1
        top, bottom = 0, m-1
        direction = 0
        i, j = 0, 0
        while head:
            grid[i][j]=head.val
            if direction%4==0:
                if j==right:
                    i+=1
                    direction+=1
                    top+=1
                else:
                    j+=1
            elif direction%4==1:
                if i==bottom:
                    j-=1
                    direction+=1
                    right-=1
                else:
                    i+=1
            elif direction%4==2:
                if j==left:
                    i-=1
                    direction+=1
                    bottom-=1
                else:
                    j-=1
            else:
                if i==top:
                    j+=1
                    direction+=1
                    left+=1
                else:
                    i-=1
            head=head.next
        return grid