class Solution:
    def longestSubstringWithNChars(self, s, n, k):
        cur_count={}
        l = 0
        have=0
        res=0
        for r in range(len(s)):
            cur_count[s[r]]=cur_count.get(s[r],0)+1
            if cur_count[s[r]]==k:
                have+=1
            while have==n and min(cur_count.values())<k:
                if cur_count[s[l]]==k:
                    have-=1
                cur_count[s[l]]-=1
                if not cur_count[s[l]]:
                    del cur_count[s[l]]
                l+=1
            if have==n:
                res=max(res,r-l+1)
        return res
            
    def longestSubstring(self, s: str, k: int) -> int:
        # find the window with n unique characters of k freq
        need = collections.Counter(s)
        return max([self.longestSubstringWithNChars(s, i, k) for i in range(1, len(need)+1)])