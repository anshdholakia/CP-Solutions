class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k>0:
            res=[]
            for i in range(len(code)):
                curres=0
                for j in range(i+1, i+k+1):
                    curres+=code[j%len(code)]
                res.append(curres)
            return res
        elif k<0:
            res=[]
            for i in range(len(code)):
                curres=0
                for j in range(i-1, (i-1)+k, -1):
                    curres+=code[j]
                res.append(curres)
            return res
        return [0]*len(code)