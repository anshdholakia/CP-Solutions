# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, inf, -inf # bool, min, max
            left, right = dfs(node.left), dfs(node.right)
            return left[2]<node.val<right[1] and left[0] and right[0], min(node.val, left[1], right[1]), max(node.val, left[2], right[2])
        return dfs(root)[0]