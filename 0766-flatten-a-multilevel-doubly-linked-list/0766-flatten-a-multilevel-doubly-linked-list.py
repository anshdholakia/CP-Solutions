"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # go through the list till you find a child
        ptr=head
        while ptr:
            if ptr.child:
                temp=ptr.next
                child=self.flatten(ptr.child)
                ptr.child=None
                ptr.next=child
                child.prev=ptr
                # get the end of list
                while child.next:
                    child=child.next
                if temp:
                    child.next=temp
                    temp.prev=child
                ptr=temp
                continue
            ptr=ptr.next
        return head
        