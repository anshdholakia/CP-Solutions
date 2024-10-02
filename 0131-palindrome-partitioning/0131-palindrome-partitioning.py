class Solution:
    def ispalindrome(self, s):
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        def backtrack(x):
            if x==len(s):
                result.append(current.copy())
                return
            for k in range(x, len(s)):
                if self.ispalindrome(s[x:k+1]):
                    current.append(s[x:k+1])
                    backtrack(k+1)
                    current.pop()
        backtrack(0)
        return result
            