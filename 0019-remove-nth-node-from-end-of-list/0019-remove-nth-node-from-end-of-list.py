# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listt=[]
        ptr=head
        length=0
        while ptr:
            listt.append(ptr)
            ptr=ptr.next
            length+=1
        if length==n:
            return head.next
        listt[length-n-1].next=listt[length-n].next
        return head

