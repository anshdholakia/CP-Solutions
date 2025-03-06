class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.freq=1
        self.left=None
        self.right=None

class DLL:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.right, self.tail.left = self.tail, self.head
        self.size=0

    def insert_head(self, node):
        self.head.right.left, node.right=node, self.head.right
        self.head.right=node
        node.left=self.head
        self.size+=1

    def remove_node(self, node):
        node.left.right, node.right.left = node.right, node.left
        self.size-=1
    
    def removeTail(self):
        tail=self.tail.left
        self.remove_node(tail)
        return tail

class LFUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.freqTable=collections.defaultdict(DLL)
        self.capacity=capacity
        self.minFreq=0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(self.cache[key], key, self.cache[key].val)
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache:
            self.updateCache(self.cache[key], key, value)
        else:
            if len(self.cache)==self.capacity:
                # remove the lfu node
                prevTail=self.freqTable[self.minFreq].removeTail()
                del self.cache[prevTail.key]
            node=Node(key, value)
            self.freqTable[1].insert_head(node)
            self.cache[key]=node
            self.minFreq=1

    def updateCache(self, node, key, val):
        node=self.cache[key]
        node.val=val
        prev_freq=node.freq
        node.freq+=1
        self.freqTable[prev_freq].remove_node(node)
        self.freqTable[node.freq].insert_head(node)
        if prev_freq==self.minFreq and self.freqTable[prev_freq].size==0:
            self.minFreq+=1
        return node.val
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)