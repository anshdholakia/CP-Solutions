class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(x, prev):
            if x==len(s):
                return True
            for i in range(x, len(s) if prev!=None else len(s)-1):
                if (prev==None or int(s[x:i+1])==prev-1) and backtrack(i+1, int(s[x:i+1])):
                    return True
            return False
        return backtrack(0, None)