"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue=collections.deque([root])
        while queue:
            link=[]
            for _ in range(len(queue)):
                pop=queue.popleft()
                link.append(pop)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            for i in range(len(link)-1):
                link[i].next=link[i+1]
        return root
