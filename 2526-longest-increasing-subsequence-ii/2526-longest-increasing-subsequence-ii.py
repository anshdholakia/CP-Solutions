class SegmentTree:
    def __init__(self, n):
        self.n=n
        self.tree=defaultdict(int)
    def query(self, L, R, idx, searchL, searchR):
        if searchR<L or R<searchL:
            return 0
        if searchL<=L and searchR>=R:
            return self.tree[idx]
        M=(L+R)//2
        leftRes, rightRes = self.query(L, M, idx*2+1, searchL, searchR), self.query(M+1, R, idx*2+2, searchL, searchR)
        return max(leftRes, rightRes)
    def update(self, L, R, idx, pos, val):
        if L==R:
            self.tree[idx]=val
            return
        m=(L+R)//2
        if pos<=m:
            self.update(L, m, idx*2+1, pos, val)
        else:
            self.update(m+1, R, idx*2+2, pos, val)
        self.tree[idx]=max(self.tree[2*idx+1], self.tree[2*idx+2])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # approach:
        # make a segment tree with range[-10**5, 10**5]
        # each node holds the count of sequence
        # keep updating the segment tree using lazy prop
        sg=SegmentTree(max(nums)+1)
        res=0
        for n in nums:
            # subtract 1 since you are dealing w 1<=n
            longest=sg.query(0, sg.n-1, 0, n-k, n-1)+1
            res=max(res, longest)
            sg.update(0, sg.n-1, 0, n, longest)
        return res