from sortedcontainers import SortedList
class Solution:

    def __init__(self, w: List[int]):
        self.sl=SortedList()
        SUM=sum(w)
        self.sum=SUM
        prevIdx=0
        for i in w:
            self.sl.add((prevIdx, i+prevIdx-1))
            prevIdx=i+prevIdx

    def pickIndex(self) -> int:
        idx=randint(0,self.sum-1)
        # use binary search to get the index
        l, r = 0, len(self.sl)-1
        while l<=r:
            m=(l+r)//2
            if self.sl[m][0]<=idx<=self.sl[m][1]:
                return m
            if self.sl[m][0]>idx:
                r=m-1
            else:
                l=m+1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()