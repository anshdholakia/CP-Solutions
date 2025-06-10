# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        cur=[]
        res=[]
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                # this is a leaf node
                cur.append(node.val)
                if sum(cur)==targetSum:
                    res.append(cur.copy())
                cur.pop()
                return
            cur.append(node.val)
            dfs(node.left)
            dfs(node.right)
            cur.pop()
        dfs(root)
        return res