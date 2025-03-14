# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums=set(nums)
        flag=False
        res=0
        while head:
            if head.val not in nums and flag:
                res+=1
                flag=False
            elif head.val in nums:
                flag=True
            head=head.next
        if flag:
            res+=1
        return res