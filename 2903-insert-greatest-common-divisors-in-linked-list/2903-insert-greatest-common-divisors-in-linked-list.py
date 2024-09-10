# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = head, head.next
        while ptr2:
            new_node = ListNode(gcd(ptr1.val, ptr2.val))
            new_node.next = ptr1.next
            ptr1.next = new_node
            ptr1=ptr2
            ptr2=ptr1.next
        return head