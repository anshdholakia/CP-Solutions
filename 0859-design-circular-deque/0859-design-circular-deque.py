class MyCircularDeque:

    def __init__(self, k: int):
        self.rear, self.front = 0, 0
        self.queue = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.rear==self.k:
            return False
        self.queue.insert(self.front, value)
        self.rear+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.rear==self.k:
            return False
        self.queue.append(value)
        self.rear+=1
        return True

    def deleteFront(self) -> bool:
        if self.rear==self.front:
            return False
        self.queue.pop(0)
        self.rear-=1
        return True

    def deleteLast(self) -> bool:
        if self.rear==self.front:
            return False
        self.queue.pop()
        self.rear-=1
        return True

    def getFront(self) -> int:
        if self.rear==self.front:
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.rear==self.front:
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        return self.rear==self.front

    def isFull(self) -> bool:
        return self.rear==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()