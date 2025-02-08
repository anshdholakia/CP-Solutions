class NumberContainers:

    def __init__(self):
        self.removed=defaultdict(set)
        self.idx_to_num=defaultdict(int)
        self.num_to_idx=defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            if index in self.removed[number]:
                self.removed[number].remove(index)
            if self.idx_to_num[index]!=number:
                self.removed[self.idx_to_num[index]].add(index)
        self.idx_to_num[index]=number
        heapq.heappush(self.num_to_idx[number], index)

    def find(self, number: int) -> int:
        while self.num_to_idx[number] and self.num_to_idx[number][0] in self.removed[number]:
            heapq.heappop(self.num_to_idx[number])
        return self.num_to_idx[number][0] if self.num_to_idx[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)