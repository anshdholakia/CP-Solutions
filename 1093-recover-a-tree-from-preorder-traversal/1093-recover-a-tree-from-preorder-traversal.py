# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack=[]
        cur_digit=0
        level=0
        dash=False
        traversal+='-'
        for i, c in enumerate(traversal):
            if c=='-':
                if dash==False:
                    while stack and stack[-1][1]>=level:
                        stack.pop()
                    node=TreeNode(cur_digit)
                    if stack:
                        if stack[-1][0].left:
                            stack[-1][0].right=node
                        else:
                            stack[-1][0].left=node
                    stack.append((node, level))
                    level=0
                level+=1
                cur_digit=0
                dash=True
            else:
                dash=False
                cur_digit=cur_digit*10+int(c)
        return stack[0][0]