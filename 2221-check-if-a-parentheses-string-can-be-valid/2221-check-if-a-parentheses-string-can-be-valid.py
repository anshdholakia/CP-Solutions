class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_max, open_min = 0, 0
        if len(s)%2:
            return False
        for b, l in zip(s, locked):
            if l=='0':
                open_max+=1
                open_min-=1
            else:
                if b=='(':
                    open_max+=1
                    open_min+=1
                else:
                    open_max-=1
                    open_min-=1
            if open_min<0:
                open_min=0
            if open_max<0:
                return False
        return open_min==0