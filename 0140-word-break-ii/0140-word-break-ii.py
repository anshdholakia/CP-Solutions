class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        res=[]
        cur=[]
        def dfs(x):
            if x==len(s):
                res.append(" ".join(cur))
                return
            for k in range(x, len(s)):
                if s[x:k+1] in wordDict:
                    cur.append(s[x:k+1])
                    dfs(k+1)
                    cur.pop()
        dfs(0)
        return res