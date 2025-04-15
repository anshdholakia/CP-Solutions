# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups=defaultdict(lambda: defaultdict(list))
        def dfs(node, key, depth):
            if not node:
                return
            groups[key][depth].append(node.val)
            dfs(node.left, key-1, depth+1)
            dfs(node.right, key+1, depth+1)
        dfs(root, 0, 0)
        return [sum([sorted(groups[k][l]) for l in sorted(groups[k].keys())], []) for k in sorted(groups.keys())]