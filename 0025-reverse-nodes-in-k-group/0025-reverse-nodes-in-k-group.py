# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseKNodes(node, k):
    a, b = node, node.next
    cur_k=1
    node.next=None
    while b and cur_k!=k:
        c=b.next
        b.next=a
        a=b
        b=c
        cur_k+=1
    return a

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = head
        ptr = head
        cur_k = 1
        endG = None
        while ptr:
            if not cur_k%k:
                nextGstart = ptr.next
                reversedG = reverseKNodes(start, k)
                if endG:
                    endG.next=reversedG
                else:
                    dummy.next=reversedG
                endG = start
                start = nextGstart
                ptr=nextGstart
                cur_k+=1
                continue
            ptr=ptr.next
            cur_k+=1
        if nextGstart:
            endG.next=nextGstart
        return dummy.next

