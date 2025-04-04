# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return depth, None
            left, right = dfs(node.left, depth+1), dfs(node.right, depth+1)
            if left[0]==right[0]:
                return left[0], node
            elif left[0]>right[0]:
                return left
            else:
                return right
        return dfs(root, 0)[1]