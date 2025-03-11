class SegmentTree:
    def __init__(self, sum, L, R):
        self.sum, self.L, self.R = sum, L, R
        self.left = None
        self.right = None
    @staticmethod
    def build(nums, L, R):
        if L==R:
            return SegmentTree(nums[L], L, R)
        M=(L+R)//2
        node=SegmentTree(0, L, R)
        node.left=SegmentTree.build(nums, L, M)
        node.right=SegmentTree.build(nums, M+1, R)
        node.sum=node.left.sum+node.right.sum
        return node
    def find_next_kth(self, k):
        # this function finds the next kth element
        if self.L==self.R:
            return self.L
        if self.left.sum>=k:
            return self.left.find_next_kth(k)
        return self.right.find_next_kth(k-self.left.sum)
    def update(self, index, val):
        if self.L==self.R:
            self.sum=val
            return
        mid=(self.L+self.R)//2
        if index>mid:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum=self.left.sum+self.right.sum

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        st=SegmentTree.build([1]*len(people), 0, len(people)-1)
        res=[None]*len(people)
        for h, p in people:
            k=st.find_next_kth(p+1)
            res[k]=[h, p]
            st.update(k, 0)
        return res
        