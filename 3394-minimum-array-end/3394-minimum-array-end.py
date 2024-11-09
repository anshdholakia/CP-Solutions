class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # fit the bits making n in the 0s places in x
        res=""
        n-=1
        while x>0 or n>0:
            while x&1:
                res+="1"
                x>>=1
            res+=str(n&1)
            n>>=1
            x>>=1
        return int(res[::-1], 2)