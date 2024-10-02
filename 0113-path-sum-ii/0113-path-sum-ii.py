# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        current = []
        def backtrack(node, cur_sum):
            if not node:
                return
            if not node.left and not node.right and cur_sum+node.val==targetSum:
                current.append(node.val)
                result.append(current.copy())
                current.pop()
                return
            current.append(node.val)
            backtrack(node.left, cur_sum+node.val)
            backtrack(node.right, cur_sum+node.val)
            current.pop()
        backtrack(root, 0)
        return result