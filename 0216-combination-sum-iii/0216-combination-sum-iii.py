class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, cur = [], []
        def backtrack(x, cur_sum):
            if cur_sum==n and len(cur)==k:
                res.append(cur.copy())
                return
            if x==0 or len(cur)>=k:
                return
            cur.append(x)
            backtrack((x+1)%10, cur_sum+x)
            cur.pop()
            backtrack((x+1)%10, cur_sum)
        backtrack(1, 0)
        return res