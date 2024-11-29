class FreqStack:

    def __init__(self):
        self.count=collections.Counter()
        self.stacks=defaultdict(list)
        self.max=0

    def push(self, val: int) -> None:
        self.count[val]+=1
        self.stacks[self.count[val]].append(val)
        self.max=max(self.max, self.count[val])

    def pop(self) -> int:
        res=self.stacks[self.max].pop()
        self.count[res]-=1
        if not self.stacks[self.max]:
            self.max=min(self.max, self.count[res])
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()