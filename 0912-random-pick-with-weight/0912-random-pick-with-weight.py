class Solution:

    def __init__(self, w: List[int]):
        self.total=sum(w)
        self.intervals=[]
        t=0
        for _, weight in enumerate(w):
            self.intervals.append((t, t+weight-1))
            t+=weight

    def pickIndex(self) -> int:
        # generate random number from 0 to self.total
        rnd=random.randint(0, self.total-1)
        # use binary search to find in intervals
        l, r = 0, len(self.intervals)-1
        while l<=r:
            m=(l+r)//2
            if rnd<self.intervals[m][0]:
                r=m-1
            elif rnd>self.intervals[m][1]:
                l=m+1
            else:
                return m



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()