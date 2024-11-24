class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # start from the target here
        # decrease the tx, ty by the smaller of the two
        while tx>sx and ty>sy:
            if (tx<ty):
                ty%=tx
            else:
                tx%=ty
        if (sx==tx) and (ty>=sy):
            return (ty-sy)%tx==0
        elif (sy==ty) and (tx>=sx):
            return (tx-sx)%ty==0
        return False