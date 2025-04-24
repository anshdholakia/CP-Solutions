class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[inf]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if j==len(word1):
                    dp[i][j]=len(word2)-i
                if i==len(word2):
                    dp[i][j]=len(word1)-j
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word2[i]==word1[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=min(1+dp[i+1][j], 1+dp[i+1][j+1], 1+dp[i][j+1])
        return dp[0][0]