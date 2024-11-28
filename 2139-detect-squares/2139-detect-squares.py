class DetectSquares:

    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        px, py = point
        res=0
        for x, y in self.points.copy():
            if abs(y-py)!=abs(x-px) or x==px or y==py: continue
            res+=(self.points[(x,py)]*self.points[(px,y)]*self.points[(x,y)])
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)