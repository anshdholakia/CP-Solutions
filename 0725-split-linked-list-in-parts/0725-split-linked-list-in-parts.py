# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        ptr = head
        while ptr:
            length+=1
            ptr=ptr.next
        part_size = length//k if length//k else 1
        remainder = length%k if length>k else 0
        ptr=head
        result = []
        for i in range(k):
            if not ptr:
                result.append(None)
            else:
                part=ptr
                for j in range(part_size-1):
                    if ptr:
                        ptr=ptr.next
                if remainder:
                    ptr=ptr.next
                    remainder-=1
                if ptr:
                    temp=ptr.next
                    ptr.next=None
                    ptr=temp
                result.append(part)
        return result