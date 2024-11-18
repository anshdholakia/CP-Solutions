# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # start from the bottom and use the node values to tag which nodes are monitored and which are unmonitored and which are monitored but dont have a camera
        result=0
        def dfs(node):
            if not node:
                return inf # return the state of node
            left, right = dfs(node.left), dfs(node.right)
            state=min(left, right) # if one is 
            if state==0: # this means the child nodes are not monitored
                nonlocal result
                node.val=1
                result+=1
                return 1
            elif state==1:
                node.val=2 # this means the child node has camera and this node is monitored
                return 2
            return min(0, state)

        dfs(root)
        return result+(root.val==0)