class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp=[[] for _ in range(len(s)+1)]
        dp[-1].append([])
        wordDict=set(wordDict)
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    for path in dp[i+len(w)]:
                        dp[i].append([s[i:i+len(w)]]+path)
        res=[]
        for path in dp[0]:
            res.append(" ".join(path))
        return res