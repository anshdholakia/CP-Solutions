class Solution:
    def smallestString(self, s: str) -> str:#
        # find s without preceding as
        i=0
        while i<len(s):
            if s[i]!='a':
                break
            i+=1
        if i==len(s):
            return s[:-1]+'z'
        # basically you need to skip a since it goes back to z
        idx=i
        while idx<len(s):
            if s[idx]=='a':
                break
            idx+=1
        def reverse(s):
            return "".join([chr(ord(c)-1) for c in s])
        return s[:i]+reverse(s[i:idx])+s[idx:]
        
        