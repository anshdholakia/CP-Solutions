# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-inf
        def dfs(node):
            if not node:
                return -inf
            left=dfs(node.left)
            right=dfs(node.right)
            nonlocal res
            res=max(res, node.val, node.val+left+right, left, right, node.val+left, node.val+right)
            return max(node.val+left, node.val+right, node.val)
        dfs(root)
        return res