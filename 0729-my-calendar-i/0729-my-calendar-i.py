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
        self.intervals.append((start, end))
        self.intervals.sort()
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)