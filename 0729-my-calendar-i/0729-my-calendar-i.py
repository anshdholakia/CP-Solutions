class TreeNode:
    def __init__(self, start, end):
        self.left, self.right = None, None
        self.start, self.end = start, end

    def insert(self, start, end):
        if end<=self.start:
            if not self.left:
                self.left=TreeNode(start, end)
                return True
            return self.left.insert(start, end)
        elif self.end<=start:
            if not self.right:
                self.right = TreeNode(start, end)
                return True
            return self.right.insert(start, end)
        return False

class MyCalendar:

    def __init__(self):
        self.root=None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root=TreeNode(startTime, endTime)
            return True
        return self.root.insert(startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)