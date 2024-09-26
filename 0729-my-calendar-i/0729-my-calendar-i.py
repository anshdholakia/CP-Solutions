class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        i = 0
        for i, (s, e) in enumerate(self.intervals):
            if s >= end:
                break
            if e <= start:
                continue
            return False
        index = bisect_left(self.intervals, end, 0, len(self.intervals), key=lambda x: x[0])
        self.intervals.insert(index, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)