class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by width
        # LIS of height
        envelope=[x[1] for x in sorted(envelopes, key=lambda x: (x[0], -x[1]))]
        stack=[]
        def binary_search(num):
            l, r = 0, len(stack)-1
            while l<=r:
                m=(l+r)//2
                if stack[m]<num:
                    l=m+1
                else:
                    r=m-1
            return l
        for h in envelope:
            if not stack or stack[-1]<h:
                stack.append(h)
            else:
                idx = binary_search(h)
                stack[idx]=h
        return len(stack)