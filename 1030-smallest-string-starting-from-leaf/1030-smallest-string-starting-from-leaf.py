# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = "z"*8500
        def backtrack(node, cur_res):
            nonlocal result
            if not node:
                return
            if not node.left and not node.right:
                cur_res+=chr(node.val+ord("a"))
                if cur_res[::-1]<result:
                    result = cur_res[::-1]
                return
            backtrack(node.left, cur_res+chr(node.val+ord("a")))
            backtrack(node.right, cur_res+chr(node.val+ord("a")))
        backtrack(root, "")
        return result