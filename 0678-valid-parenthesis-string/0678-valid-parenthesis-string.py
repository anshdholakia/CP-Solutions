class Solution:
    def checkValidString(self, s: str) -> bool:
        pos_minimum, pos_maximum = 0, 0
        for i in s:
            if i=='(':
                pos_maximum+=1
                pos_minimum+=1
            elif i=='*':
                pos_minimum-=1
                pos_maximum+=1
            else:
                pos_minimum-=1
                pos_maximum-=1
            if pos_maximum<0:
                return False
            if pos_minimum<0:
                pos_minimum=0
        return pos_minimum==0
        


