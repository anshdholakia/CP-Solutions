# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        cur_k=1
        ptr=head
        group_start=head
        prev_end=None
        def reverse(start, end):
            a, b = start, start.next
            a.next=None
            while a!=end:
                c=b.next
                b.next=a
                a=b
                b=c
            return a
        while ptr:
            if cur_k%k==0:
                new_start=ptr.next
                reversed_group=reverse(group_start, ptr)
                if not dummy.next:
                    dummy.next=reversed_group
                if prev_end:
                    prev_end.next=reversed_group
                prev_end=group_start
                group_start=new_start
                ptr=new_start
                cur_k+=1
                continue
            cur_k+=1
            ptr=ptr.next
        if new_start:
            prev_end.next=new_start
        return dummy.next