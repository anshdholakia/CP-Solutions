from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.sorted_list = SortedList()
        self.nums = deque()
        self.total = 0
        self.kBig, self.kSmall = 0, 0

    def addElement(self, num: int) -> None:
        # check adding this element to the list
        self.total+=num
        self.nums.append(num)
        idx=self.sorted_list.bisect_left(num)
        if idx<self.k:
            self.kSmall+=num
            if len(self.sorted_list)>=self.k:
                self.kSmall-=self.sorted_list[self.k-1]
        if idx>=len(self.sorted_list)-self.k+1:
            self.kBig+=num
            if len(self.sorted_list)>=self.k:
                self.kBig-=self.sorted_list[-self.k]
        self.sorted_list.add(num)
        # handle nums to be removed from sliding window
        if len(self.nums)>self.m:
            toRemove=self.nums.popleft()
            self.total-=toRemove
            idx=self.sorted_list.index(toRemove)
            if idx<self.k:
                self.kSmall-=toRemove
                self.kSmall+=self.sorted_list[self.k]
            elif idx>=len(self.sorted_list)-self.k:
                self.kBig-=toRemove
                self.kBig+=self.sorted_list[-self.k-1]
            self.sorted_list.remove(toRemove)

    def calculateMKAverage(self) -> int:
        if len(self.nums)<self.m:
            return -1
        return (self.total-self.kSmall-self.kBig)//(self.m-2*self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()