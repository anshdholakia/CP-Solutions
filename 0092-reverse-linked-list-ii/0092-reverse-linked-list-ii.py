# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node):
            cur_k=0
            a, b = node, node.next
            while b and cur_k!=right-left:
                c=b.next
                b.next=a
                a=b
                b=c
                cur_k+=1
            node.next=b
            return a
        i=1
        prev=None
        ptr=head
        while ptr:
            if i==left:
                node=reverse(ptr)
                if prev:
                    prev.next=node
                    return head
                else:
                    return node
            i+=1
            prev=ptr
            ptr=ptr.next
        return head
