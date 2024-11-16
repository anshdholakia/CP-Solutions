# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result=[]
        def find_downward_nodes(node, dist):
            if not node:
                return
            if dist==0:
                result.append(node.val)
                return
            find_downward_nodes(node.left, dist-1)
            find_downward_nodes(node.right, dist-1)
        def helper(node):
            if not node:
                return -1
            if node==target:
                find_downward_nodes(node, k)
                return 1
            left_call=helper(node.left)
            if left_call==k:
                result.append(node.val)
                return left_call+1
            elif left_call!=-1:
                find_downward_nodes(node.right, k-left_call-1)
                return left_call+1
            right_call=helper(node.right)
            if right_call==k:
                result.append(node.val)
                return right_call+1
            elif right_call!=-1:
                find_downward_nodes(node.left, k-right_call-1)
                return right_call+1
            return -1
        helper(root)
        return result