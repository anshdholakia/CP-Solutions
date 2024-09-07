# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, ptr):
        if not node:
            return ptr==None
        if not ptr:
            return True
        return node.val==ptr.val and (self.dfs(node.left, ptr.next) or self.dfs(node.right, ptr.next))

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        result = False
        def bfs(node):
            nonlocal result
            if result:
                return
            if not node:
                return
            if node.val==head.val:
                result = result or self.dfs(node, head)
            bfs(node.left)
            bfs(node.right)
        bfs(root)
        return result
            

            
                