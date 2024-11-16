# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        # merge the two linked lists
        final=ptr=None
        while l1 and l2:
            if l1.val<l2.val:
                if not final:
                    final=ptr=l1
                else:
                    ptr.next=l1
                    ptr=ptr.next
                l1=l1.next
            else:
                if not final:
                    final=ptr=l2
                else:
                    ptr.next=l2
                    ptr=ptr.next
                l2=l2.next
        if l1:
            if not final:
                final=ptr=l1
            else:
                ptr.next=l1
        if l2:
            if not final:
                final=ptr=l2
            else:
                ptr.next=l2
        return final
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        if not head:
            return head
        slow, fast = head, head.next
        if not fast: # this means the length is only 1
            return slow
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        l1, l2 = self.sortList(head), self.sortList(temp)
        return self.merge(l1, l2)

        
        