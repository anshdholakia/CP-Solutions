# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKNodes(node, end):
            a=node
            b=node.next
            a.next=None
            while a!=end:
                c=b.next
                b.next=a
                a=b
                b=c
            return a

        dummy=ListNode()
        dummy.next=None
        cur_k=1
        curGroupStart=head
        prevGroupEnd=None
        while head:
            if not cur_k%k:
                curGroupEnd=head
                head=head.next
                curGroupEnd.next=None
                #reverse the nodes
                groupStart=reverseKNodes(curGroupStart, curGroupEnd)
                if not dummy.next:
                    dummy.next=groupStart
                if prevGroupEnd:
                    prevGroupEnd.next=groupStart
                prevGroupEnd=curGroupStart
                curGroupStart=head
                cur_k+=1
                continue
            cur_k+=1
            head=head.next
        if prevGroupEnd:
            prevGroupEnd.next=curGroupStart
        return dummy.next
        