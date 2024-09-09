# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = collections.deque(lists)
        if not queue:
            return None
        while len(queue)!=1:
            l1 = queue.popleft()
            l2 = queue.popleft()
            result = ptr = None
            while l1 and l2:
                if l1.val<l2.val:
                    if not result:
                        ptr=result=l1
                    else:
                        ptr.next=l1
                        ptr=ptr.next
                    l1=l1.next
                else:
                    if not result:
                        ptr=result=l2
                    else:
                        ptr.next=l2
                        ptr=ptr.next
                    l2=l2.next
            while l1:
                if not result:
                    result=ptr=l1
                else:
                    ptr.next = l1
                    ptr=ptr.next
                l1=l1.next
            while l2:
                if not result:
                    result=ptr=l2
                else:
                    ptr.next=l2
                    ptr=ptr.next
                l2=l2.next
            if ptr:
                ptr.next=None
            queue.append(result)
        return queue[0]