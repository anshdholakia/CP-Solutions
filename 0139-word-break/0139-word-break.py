class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        @cache
        def dp(i):
            if i==len(s):
                return True
            res=False
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)] in wordDict:
                    res=res or dp(i+len(word))
                    if res:
                        return True
            return res
        return dp(0)