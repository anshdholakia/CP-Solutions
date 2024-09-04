# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head
        while ptr:
            while stack and stack[-1].val<ptr.val:
                stack.pop()
            stack.append(ptr)
            ptr=ptr.next
        if not stack:
            return None
        head = stack[0]
        ptr = head
        for i in range(1, len(stack)):
            ptr.next = stack[i]
            ptr=ptr.next
        ptr.next = None
        return head