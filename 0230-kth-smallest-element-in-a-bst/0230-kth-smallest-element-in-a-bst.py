# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        cur_k=0
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            while stack:
                popped=stack.pop()
                cur_k+=1
                if cur_k==k:
                    return popped.val
                if popped.right:
                    root=popped.right
                    break