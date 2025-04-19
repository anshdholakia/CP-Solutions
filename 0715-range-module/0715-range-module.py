class SegmentTree:
    # Segment tree with lazy propagation
    # 1. Check if the current node has a lazy update to be made
    # 2. If it has, do the lazy update and propagate to its immediate children
    # 3. Then check if the range of the node completely overlaps with the query
    # 4. If it does, return the node value
    # 5. If it does not, recursive call to left and right children if it partially overlaps only
    def __init__(self):
        self.n=10**9
        self.tree, self.lazy=defaultdict(int), defaultdict(lambda:None) # None, True, False
    def update(self, L, R, idx, val, qleft, qright):
        # check lazy propagation
        if self.lazy[idx]!=None:
            # propagate this
            self.tree[idx]=self.lazy[idx]
            if L!=R:
                self.lazy[idx*2+1]=self.lazy[idx]
                self.lazy[idx*2+2]=self.lazy[idx]
            # remove lazy
            self.lazy[idx]=None
        if qright<L or qleft>R:
            return
        if qleft<=L and R<=qright:
            self.tree[idx]=self.lazy[idx]=val
            return
        M=(L+R)//2
        self.update(L, M, 2*idx+1, val, qleft, qright)
        self.update(M+1, R, 2*idx+2, val, qleft, qright)
        self.tree[idx]=self.tree[idx*2+1]&self.tree[idx*2+2]
    def query(self, L, R, idx, qleft, qright):
        # check lazy propagation
        if self.lazy[idx]!=None:
            # propagate this
            self.tree[idx]=self.lazy[idx]
            if L!=R:
                self.lazy[idx*2+1]=self.lazy[idx]
                self.lazy[idx*2+2]=self.lazy[idx]
            # remove lazy
            self.lazy[idx]=None
        if qright<L or qleft>R:
            return True
        if qleft<=L and R<=qright:
            return self.tree[idx]
        M=(L+R)//2
        left=self.query(L, M, 2*idx+1, qleft, qright)
        right=self.query(M+1, R, 2*idx+2, qleft, qright)
        return left&right
    
class RangeModule:

    def __init__(self):
        self.sg = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.sg.update(0, self.sg.n, 0, 1, left, right-1) # sets 1 to the range [left, right)

    def queryRange(self, left: int, right: int) -> bool:
        # check is the query range sums to the number of elements
        return self.sg.query(0, self.sg.n, 0, left, right-1)==1

    def removeRange(self, left: int, right: int) -> None:
        self.sg.update(0, self.sg.n, 0, 0, left, right-1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)