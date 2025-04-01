class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        result=1
        def backtrack(i, j):
            # s[:i+1]+t[j:]
            final=s[:i+1]+t[j:]
            # find the largest palindrome here
            for m in range(len(final)):
                l, r = m-1, m+1
                nonlocal result
                while r<len(final) and final[r]==final[m]:
                    result=max(result, r-m+1)
                    r+=1
                while l>=0 and r<len(final) and final[l]==final[r]:
                    result=max(result, r-l+1)
                    l-=1
                    r+=1
        for i in range(-1, len(s)):
            for j in range(len(t)+1):
                backtrack(i, j)
        return result