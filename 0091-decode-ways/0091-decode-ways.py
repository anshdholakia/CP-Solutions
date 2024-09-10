class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if i==len(s)-1:
                return 1
            if 0<int(s[i:i+2])<=26:
                memo[i]= dfs(i+1)+dfs(i+2)
                return memo[i]
            memo[i]= dfs(i+1)
            return memo[i]
        return dfs(0)