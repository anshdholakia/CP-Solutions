# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ptr = root
        while ptr:
            if ptr.val<p.val and ptr.val<q.val:
                ptr=ptr.right
            elif ptr.val>p.val and ptr.val>q.val:
                ptr=ptr.left
            else:
                return ptr