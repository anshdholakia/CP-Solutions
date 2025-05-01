class DetectSquares:

    def __init__(self):
        self.freq=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        # get the diagonals
        x, y = point
        res=0
        self.freq[(x, y)]+=1
        for q1, q2 in self.freq:
            if q1!=x and q2!=y and abs(x-q1)==abs(y-q2) and (q1, y) in self.freq and (x, q2) in self.freq:
                res+=(self.freq[(q1, y)]*self.freq[(x, q2)]*self.freq[(q1, q2)])
        self.freq[(x, y)]-=1
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)