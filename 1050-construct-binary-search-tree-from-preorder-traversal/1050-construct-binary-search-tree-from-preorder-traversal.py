# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node=TreeNode(preorder[0])
        # iterate while you find bigger than root
        idx=1
        while idx<len(preorder):
            if preorder[idx]>node.val:
                break
            idx+=1
        node.left=self.bstFromPreorder(preorder[1:idx])
        node.right=self.bstFromPreorder(preorder[idx:])
        return node