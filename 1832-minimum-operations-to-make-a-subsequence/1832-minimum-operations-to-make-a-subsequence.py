class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # this is basically a longest increasing subsequence question. Mark all the elements in target with the index in arr
        elemToIdx={e:idx for idx, e in enumerate(target)}
        arr=[elemToIdx[x] for x in arr if x in elemToIdx]
        # now do LIS in arr
        stack=[]
        for n in arr:
            if not stack or stack[-1]<n:
                stack.append(n)
            else:
                idx=bisect_left(stack, n)
                stack[idx]=n
        return len(target)-len(stack)