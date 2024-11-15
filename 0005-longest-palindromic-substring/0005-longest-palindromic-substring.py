class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        # using 2d dynamic programming with its own string
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            res=s[i:i+1]
            dp[i][i]=True
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]==True:
                        # check left bottom cell since it is in the inner substring
                        dp[i][j]=True
                        if len(res)<len(s[i:j+1]):
                            res=s[i:j+1]
        return res