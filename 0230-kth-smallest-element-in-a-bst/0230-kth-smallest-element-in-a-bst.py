# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # preorder traversal
        cur_k=0
        def dfs(node):
            nonlocal cur_k
            if not node:
                return
            res1=dfs(node.left)
            cur_k+=1
            if cur_k==k:
                return node
            res2=dfs(node.right)
            return res1 or res2
        return dfs(root).val