class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur=[]
        res=[]
        def backtrack(idx):
            if idx==len(s):
                res.append(cur.copy())
                return
            for i in range(idx, len(s)):
                if s[idx:i+1]==s[idx:i+1][::-1]:
                    cur.append(s[idx:i+1])
                    backtrack(i+1)
                    cur.pop()
        backtrack(0)
        return res