from threading import Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.insert_lock, self.remove_lock = Lock(), Lock()
        self.queue=collections.deque([])
        self.capacity=capacity
        self.remove_lock.acquire() # dont remove yet

    def enqueue(self, element: int) -> None:
        self.insert_lock.acquire()
        self.queue.append(element)
        if len(self.queue)<self.capacity:
            self.insert_lock.release()
        if self.remove_lock.locked():
            self.remove_lock.release()

    def dequeue(self) -> int:
        self.remove_lock.acquire()
        element=self.queue.popleft()
        if len(self.queue)>0:
            self.remove_lock.release()
        if self.insert_lock.locked():
            self.insert_lock.release()
        return element
        
    def size(self) -> int:
        return len(self.queue)