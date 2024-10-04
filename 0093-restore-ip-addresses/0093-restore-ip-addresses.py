class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        cur = []
        def backtrack(x):
            if len(cur)>4:
                return
            if x==len(s) and len(cur)==4:
                result.append(".".join(cur))
                return
            # get the numbers which are in the range 0 to 255
            for i in range(3):
                if x+i+1<=len(s) and 0<=int(s[x:x+i+1])<=255:
                    if i>=1 and s[x:x+i+1].startswith("0"):
                        continue
                    cur.append(s[x:x+i+1])
                    backtrack(x+i+1)
                    cur.pop()
        backtrack(0)
        return result