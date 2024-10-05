# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        queue = collections.deque([(root, 0)])
        result = []
        while queue:
            for _ in range(len(queue)):
                pnode, pval = queue.popleft()
                if pnode:
                    hashmap[pval].append(pnode.val)
                    queue.append((pnode.left, pval-1))
                    queue.append((pnode.right, pval+1))
        for key in sorted(hashmap.keys()):
            result.append(hashmap[key])
        return result