class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*(len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            dp[i]=max(questions[i][0]+(dp[questions[i][1]+i+1] if questions[i][1]+i+1<len(questions) else 0), dp[i+1])
        return max(dp)