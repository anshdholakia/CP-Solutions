# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.child=[self.root]
        queue=collections.deque([root])
        level=0
        self.idx=0
        while queue:
            level+=1
            new_child=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    new_child.append(node.left)
                    queue.append(node.left)
                if node.right:
                    new_child.append(node.right)
                    queue.append(node.right)
            if len(new_child)==2**level:
                self.child=new_child
        # move idx to the right node
        for node in self.child:
            if not node.left or not node.right:
                break
            self.idx+=1

    def insert(self, val: int) -> int:
        # when the next set of nodes are filled
        # update the self.child
        new_node=TreeNode(val)
        while self.idx<len(self.child):
            insert_in=self.child[self.idx]
            if not insert_in.left:
                insert_in.left=new_node
                return insert_in.val
            elif not insert_in.right:
                insert_in.right=new_node
                return insert_in.val
            else:
                self.idx+=1
            if self.idx==len(self.child):
                self.__init__(self.root)

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()