# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cache=defaultdict(lambda:defaultdict(list))
        def dfs(node, idx, depth):
            if not node:
                return
            cache[idx][depth].append(node.val)
            dfs(node.left, idx-1, depth+1)
            dfs(node.right, idx+1, depth+1)
        dfs(root, 0, 0)
        return [sum([sorted(cache[idx][d]) for d in sorted(cache[idx].keys())],[]) for idx in sorted(cache.keys())]