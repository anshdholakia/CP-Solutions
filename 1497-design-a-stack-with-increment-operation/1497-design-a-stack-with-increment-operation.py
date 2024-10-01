class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.additions = [0 for _ in range(maxSize)] # hold increment val at k as the index

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        result = self.stack.pop() + self.additions[index]
        if index > 0:
            self.additions[index - 1] += self.additions[index]
        self.additions[index] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.additions[min(len(self.stack), k)-1]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)