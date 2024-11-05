class SegmentTree:
    def __init__(self, L, R, total=0):
        self.total=total
        self.L=L
        self.R=R
        self.left=None
        self.right=None
    @staticmethod
    def build(L, R, nums):
        if L==R:
            return SegmentTree(L, R, nums[L])
        node=SegmentTree(L, R)
        M=(L+R)//2
        node.left=SegmentTree.build(L, M, nums)
        node.right=SegmentTree.build(M+1, R, nums)
        node.total=(node.left.total+node.right.total)
        return node
    def update(self, idx, new_val):
        if self.L==idx and self.R==idx:
            self.total=new_val
            return
        M=(self.L+self.R)//2
        if idx<=M:
            self.left.update(idx, new_val)
        else:
            self.right.update(idx, new_val)
        self.total=self.left.total+self.right.total
    def range_query(self, left, right):
        if left==self.L and right==self.R:
            return self.total
        M=(self.L+self.R)//2
        if right<=M:
            return self.left.range_query(left, right)
        elif left>M:
            return self.right.range_query(left, right)
        return self.left.range_query(left, M)+self.right.range_query(M+1, right)

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree.build(0, len(nums)-1, nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.range_query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)