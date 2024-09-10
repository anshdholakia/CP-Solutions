class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(dp)):
            for word in wordDict:
                if i+len(word)<len(dp) and s[i:i+len(word)]==word:
                    dp[i+len(word)] = dp[i+len(word)] or dp[i]
        return dp[-1]
            