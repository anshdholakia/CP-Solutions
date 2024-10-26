# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # keep max 2 heights at each level
        treeHeights = {}
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            treeHeights[node.val]=max(left, right)+1
            return treeHeights[node.val]
        dfs(root)
        # get max 2 heights at each level
        queue = collections.deque([])
        nodeLevels = {}
        levelMaxs = {}
        queue.append(root)
        level=-1
        while queue:
            level+=1
            max1, max2 = -1, -1
            for _ in range(len(queue)):
                pop=queue.popleft()
                nodeLevels[pop.val]=level
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                if treeHeights[pop.val]>max1:
                    max1, max2 = treeHeights[pop.val], max1
                elif treeHeights[pop.val]>max2:
                    max2 = treeHeights[pop.val]
            levelMaxs[level] = [max1, max2]
        memo = {}
        res = []
        for q in queries:
            if q in memo:
                res.append(memo[q])
                continue
            rootHeight=treeHeights[root.val]
            nodeLevel=nodeLevels[q]
            if treeHeights[q]==levelMaxs[nodeLevel][0]:
                rootHeight=rootHeight-levelMaxs[nodeLevel][0]+levelMaxs[nodeLevel][1]
            memo[q]=rootHeight
            res.append(memo[q])
        return res
