class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        dp=[inf]*(len(s)+1)
        dp[-1]=0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    dp[i]=min(dp[i], dp[j+1])
                else:
                    dp[i]=min(dp[i], dp[i+1]+1)
        return dp[0]