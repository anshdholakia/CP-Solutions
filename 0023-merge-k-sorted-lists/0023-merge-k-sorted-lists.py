# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            ptr=new=None
            while l1 and l2:
                if l1.val<l2.val:
                    if not new:
                        new=ptr=l1
                    else:
                        ptr.next=l1
                        ptr=ptr.next
                    l1=l1.next
                else:
                    if not new:
                        new=ptr=l2
                    else:
                        ptr.next=l2
                        ptr=ptr.next
                    l2=l2.next
            ptr.next=l2 or l1
            return new
        while len(lists)>1:
            new_lists=[]
            for i in range(0, len(lists), 2):
                if i+1<len(lists):
                    new_lists.append(merge(lists[i], lists[i+1]))
                else:
                    new_lists.append(lists[i])
            lists=new_lists
        return lists[0] if lists else None