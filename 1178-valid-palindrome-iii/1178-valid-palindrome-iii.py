class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def dfs(cur_k, l, r):
            if cur_k>k:
                return False
            while l<r:
                if s[l]!=s[r]:
                    # you have two choices here
                    return dfs(cur_k+1, l, r-1) or dfs(cur_k+1, l+1, r)
                l+=1
                r-=1
            return True
        return dfs(0, 0, len(s)-1)