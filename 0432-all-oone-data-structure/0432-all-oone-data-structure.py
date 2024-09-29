class AllOne:

    def __init__(self):
        self.counter = {}
        self.minheap = []
        self.maxheap = []

    def inc(self, key: str) -> None:
        self.counter[key] = self.counter.get(key, 0)+1
        heapq.heappush(self.minheap, (self.counter[key], key))
        heapq.heappush(self.maxheap, (-self.counter[key], key))

    def dec(self, key: str) -> None:
        self.counter[key]-=1
        if self.counter[key]==0:
            del self.counter[key]
            return
        heapq.heappush(self.minheap, (self.counter[key], key))
        heapq.heappush(self.maxheap, (-self.counter[key], key))

    def getMaxKey(self) -> str:
        while self.maxheap and (self.maxheap[0][1] not in self.counter or -self.maxheap[0][0]!=self.counter[self.maxheap[0][1]]):
            heapq.heappop(self.maxheap)
        return self.maxheap[0][1] if self.maxheap else ""
        
    def getMinKey(self) -> str:
        while self.minheap and (self.minheap[0][1] not in self.counter or self.minheap[0][0]!=self.counter[self.minheap[0][1]]):
            heapq.heappop(self.minheap)
        return self.minheap[0][1] if self.minheap else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()