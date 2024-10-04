class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        current=[]
        def backtrack(cur_x, cur_k):
            if cur_k==k:
                result.append(current.copy())
                return
            if cur_x==n+1:
                return
            for i in range(cur_x, n+1):
                current.append(i)
                backtrack(i+1, cur_k+1)
                current.pop()
        backtrack(1, 0)
        return result