# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use hashmap to club the nodes and subtract its val with total
        queue=collections.deque([root])
        while queue:
            cur_sum = 0
            valGrp = defaultdict(list) # holds the total value of group to list of nodes
            for _ in range(len(queue)):
                psum = 0
                pop = queue.popleft()
                if pop.left:
                    psum+=pop.left.val
                    cur_sum+=pop.left.val
                    queue.append(pop.left)
                if pop.right:
                    psum+=pop.right.val
                    cur_sum+=pop.right.val
                    queue.append(pop.right)
                if pop.left:
                    valGrp[psum].append(pop.left)
                if pop.right:
                    valGrp[psum].append(pop.right)
            for k, v in valGrp.items():
                for node in v:
                    node.val=cur_sum-k
        root.val = 0
        return root
            
            
