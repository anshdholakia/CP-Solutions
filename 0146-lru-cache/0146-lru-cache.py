class Node:
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.left, self.right = Node(-1), Node(-1)
        self.left.right, self.right.left = self.right, self.left

    def update(self, key):
        # shift this node to start
        node=self.key_to_node[key]
        node.left.right, node.right.left = node.right, node.left
        node.left, node.right = self.right.left, self.right
        self.right.left.right, self.right.left = node, node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        self.update(key)
        ptr=self.left
        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.update(key)
            self.key_to_node[key].val=value
            return
        # add the node to start and then look at capacity for removal
        self.key_to_node[key] = node = Node(key, value, self.left, self.left.right)
        node.left.right, node.right.left = node, node
        if self.right.left!=node:
            self.update(key)
        if len(self.key_to_node)>self.capacity:
            # remove the left node here
            node = self.left.right
            node.left.right, node.right.left = node.right, node.left
            node.left, node.right = None, None
            del self.key_to_node[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)