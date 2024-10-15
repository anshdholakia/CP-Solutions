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
        # get the middle of te lst
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # start reversing the second half of the list
        a, b = slow, slow.next
        while b:
            c=b.next
            b.next=a
            a=b
            b=c

        ptr1 = head
        while ptr1!=a:
            temp1 = a.next
            temp2 = ptr1.next
            a.next = ptr1.next
            ptr1.next = a
            a = temp1
            ptr1 = temp2
        ptr1.next=None
        return head
