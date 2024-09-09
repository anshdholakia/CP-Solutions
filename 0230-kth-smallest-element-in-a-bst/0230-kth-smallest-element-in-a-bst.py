# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        stack.append(root)
        cur_k = 0
        while stack:
            while stack[-1].left:
                stack.append(stack[-1].left)
            while stack:
                popped = stack.pop()
                cur_k+=1
                if cur_k==k:
                    return popped.val
                if popped.right:
                    stack.append(popped.right)
                    break
