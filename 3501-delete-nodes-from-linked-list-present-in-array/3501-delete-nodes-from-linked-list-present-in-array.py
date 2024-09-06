# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        ptr = head
        while ptr:
            if ptr.val not in nums:
                break
            ptr = ptr.next
            head = ptr
        p1, p2 = head, head.next
        while p2:
            if p2.val in nums:
                # delete
                p1.next=p2.next
                p2=p2.next
                continue
            p2=p2.next
            p1=p1.next
        return head