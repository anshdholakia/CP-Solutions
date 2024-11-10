class Solution:
    def intToRoman(self, num: int) -> str:
        mapping={
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        res=[]
        idx=0
        def convert(num):
            if num in mapping:
                return mapping[num]
            start_num=None
            powers=-1
            while num:
                powers+=1
                start_num=num%10
                num//=10
            print(powers, start_num)
            if start_num==2 or start_num==3:
                return mapping[10**powers]*start_num
            elif start_num==4:
                return mapping[10**powers]+mapping[5*(10**powers)]
            elif start_num==6:
                return mapping[5*10**powers]+mapping[10**powers]
            elif start_num==7:
                return mapping[5*10**powers]+mapping[10**powers]+mapping[10**powers]
            elif start_num==8:
                return mapping[5*10**powers]+mapping[10**powers]+mapping[10**powers]+mapping[10**powers]
            elif start_num==9:
                return mapping[10**powers]+mapping[10**(powers+1)]
        if num in mapping:
            return mapping[num]
        while num:
            curres=convert(num%10*(10**idx))
            if curres:
                res.append(curres)
            num//=10
            idx+=1
        return "".join(res[::-1]) 