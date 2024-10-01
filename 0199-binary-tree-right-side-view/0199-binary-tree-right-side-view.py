# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            cur_res = None
            for _ in range(len(queue)):
                popped = queue.popleft()
                if not cur_res:
                    cur_res = popped
                if popped.right:
                    queue.append(popped.right)
                if popped.left:
                    queue.append(popped.left)
            if cur_res:
                result.append(cur_res.val)
        return result