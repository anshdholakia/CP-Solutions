class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        target = collections.Counter(t)
        result = float("inf")
        current = {}
        result_str = ""
        have, need = 0, len(target)
        for r in range(len(s)):
            if s[r] in target:
                current[s[r]] = current.get(s[r], 0) + 1
                if current[s[r]]==target[s[r]]:
                    have+=1
                while have==need:
                    if result>r-l+1:
                        result=r-l+1
                        result_str = s[l:r+1]
                    if s[l] in target:
                        current[s[l]]-=1
                        if current[s[l]]<target[s[l]]:
                            have-=1
                    l+=1
        return result_str