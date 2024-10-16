# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # reverse right subtree
        def reverse(node):
            if not node:
                return
            node.left, node.right = reverse(node.right), reverse(node.left)
            return node
        rr = reverse(root.right)
        p, q = root.left, rr
        def check(st1, st2):
            if not st1 and not st2:
                return True
            if not st1 or not st2:
                return False
            return st1.val==st2.val and check(st1.left, st2.left) and check(st1.right, st2.right)
        return check(p, q)
        