# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split the head and put in one by one
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        if not head2:
            return
        slow.next=None
        # reverse this head2
        a, b = head2, head2.next
        a.next=None
        while b:
            c=b.next
            b.next=a
            a=b
            b=c
        head2=a
        ptr1, ptr2 = head, head2
        while ptr1 and ptr2:
            temp_behind=ptr2.next
            temp=ptr1.next
            ptr1.next=ptr2
            ptr2.next=temp
            ptr1=temp
            ptr2=temp_behind
        