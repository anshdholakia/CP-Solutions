class ListNode:
    def __init__(self, key=None, val=None):
        self.key=key
        self.val=val
        self.left, self.right = None, None

class LRU:
    def __init__(self):
        self.left, self.right = ListNode(), ListNode()
        self.left.right, self.right.left = self.right, self.left
    def remove(self, node):
        node.left.right, node.right.left = node.right, node.left
    def add(self, node):
        if self.left.right==self.right and self.right.left==self.left:
            self.left.right, self.right.left = node, node
            node.left, node.right = self.left, self.right
        else:
            self.right.left.right, self.right.left, node.left, node.right = node, node, self.right.left, self.right
    def empty(self):
        return self.left.right==self.right and self.right.left==self.left
    def remove_left(self):
        ret = self.left.right.key
        self.remove(self.left.right)
        return ret

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.all_nodes={}
        self.node_to_count={}
        self.count_to_lru=defaultdict(lambda: LRU())
        self.min_key=1

    def get(self, key: int) -> int:
        if key in self.all_nodes:
            cur=self.node_to_count[key]
            self.count_to_lru[cur].remove(self.all_nodes[key])
            if self.count_to_lru[self.min_key].empty():
                self.min_key+=1
            self.node_to_count[key]+=1
            self.count_to_lru[self.node_to_count[key]].add(self.all_nodes[key])
            return self.all_nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.all_nodes:
            if len(self.all_nodes)==self.capacity:
                # remove node from self.min_key before adding
                removed=self.count_to_lru[self.min_key].remove_left()
                del self.all_nodes[removed]
                del self.node_to_count[removed]
            self.all_nodes[key]=ListNode(key, value)
            self.min_key=1
            self.count_to_lru[1].add(self.all_nodes[key])
            self.node_to_count[key]=1
        else:
            self.all_nodes[key].val=value
            cur=self.node_to_count[key]
            self.count_to_lru[cur].remove(self.all_nodes[key])
            if self.count_to_lru[self.min_key].empty():
                self.min_key+=1
            self.count_to_lru[cur+1].add(self.all_nodes[key])
            self.node_to_count[key]+=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)