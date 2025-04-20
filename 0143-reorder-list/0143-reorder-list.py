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
        # split the list
        slow, fast = head, head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        half=slow.next
        slow.next=None
        if not half:
            return
        # reverse half
        a, b = half, half.next
        a.next=None
        while b:
            c=b.next
            b.next=a
            a=b
            b=c
        ptr1, ptr2 = head, a
        while ptr1 and ptr2:
            temp1, temp2 = ptr1.next, ptr2.next
            ptr1.next=ptr2
            ptr2.next=temp1
            ptr1, ptr2 = temp1, temp2
