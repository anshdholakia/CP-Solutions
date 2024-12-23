# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res=0
        queue=collections.deque([root])
        def check(level):
            sort_level = sorted(level)
            mp = {v: i for i, v in enumerate(level)}
            operations=0
            for i in range(len(level)):
                while level[i] != sort_level[i]:
                    operations += 1
                    cur = mp[sort_level[i]]
                    mp[level[i]] = cur
                    level[i], level[cur] = level[cur], level[i]
            return operations
        while queue:
            level=[]
            for _ in range(len(queue)):
                pop=queue.popleft()
                if not pop:
                    continue
                level.append(pop.val)
                queue.append(pop.left)
                queue.append(pop.right)
            res+=check(level)
        return res