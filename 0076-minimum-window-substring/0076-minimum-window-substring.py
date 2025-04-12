class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target=collections.Counter(t)
        need=len(target)
        have=0
        result=""
        res_len=inf
        l=0
        count={}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            if count[s[r]]==target[s[r]]:
                have+=1
            while have==need:
                if r-l+1<res_len:
                    res_len=r-l+1
                    result=s[l:r+1]
                count[s[l]]-=1
                if s[l] in target and count[s[l]]<target[s[l]]:
                    have-=1
                l+=1
        return result