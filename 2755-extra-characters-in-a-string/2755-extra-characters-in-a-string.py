class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = [len(s)]*len(s) + [0]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s), i, -1):
                if s[i:j] in dictionary:
                    dp[i] = min(dp[j], dp[i])
            dp[i] = min(dp[i+1]+1, dp[i])
        return dp[0]