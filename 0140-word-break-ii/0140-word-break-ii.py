class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cur_res=[]
        result=[]
        wordDict=set(wordDict)
        def dfs(i):
            if i==len(s):
                result.append(" ".join(cur_res))
                return
            for k in range(i, len(s)):
                if s[i:k+1] in wordDict:
                    cur_res.append(s[i:k+1])
                    dfs(k+1)
                    cur_res.pop()
        dfs(0)
        return result