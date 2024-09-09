# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=-float("inf")
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            result=max(result, left+node.val, right+node.val, left+right+node.val, node.val)
            return max(left+node.val, right+node.val, node.val)
        dfs(root)
        return result