# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # morris traversal
        # make the leaf nodes predecesor point to the root of the tree
        # and then initialize the self.start to the first left
        ptr=root
        while ptr.left:
            ptr=ptr.left
        self.start=ptr
        def find_pred(node):
            left=node.left
            while left.right and left.right!=node:
                left=left.right
            return left
        def find_pred2(node):
            right=node.right
            while right and right.left and right.left!=node:
                right=right.left
            return right
        while root:
            if root.left==None:
                pred=find_pred2(root)
                temp=root.right
                root.right=pred
                root=temp
            else:
                pred=find_pred(root)
                pred.right=root
                root.left, root = None, root.left
                
    def next(self) -> int:
        val=self.start.val
        self.start=self.start.right
        return val

    def hasNext(self) -> bool:
        return bool(self.start!=None)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()