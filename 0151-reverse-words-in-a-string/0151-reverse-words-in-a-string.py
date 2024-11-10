class Solution:
    def reverseWords(self, s: str) -> str:
        startidx=0
        curwordlen=0
        space=False
        letter=False
        for i in range(len(s)-1,-1,-1):
            if s[-1]==' ' and not space and letter:
                startidx+=curwordlen
                s=s[:startidx]+' '+s[startidx:-1]
                curwordlen=0
                space=True
                startidx+=1
                letter=False
                continue
            elif s[-1]==' ':
                s=s[:startidx]+s[startidx:-1]
                continue
            s=s[:startidx]+s[-1]+s[startidx:-1]
            space=False
            letter=True
            curwordlen+=1
        if letter==False:
            s=s[:-1]
        return s