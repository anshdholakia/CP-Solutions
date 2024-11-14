class Solution:
    def calculate(self, s: str) -> int:
        i=0
        s=s.replace(" ","")
        s+='#'
        cur_op='+'
        res, prev, digit = 0, 0, 0
        while i<len(s):
            if s[i].isdigit():
                digit=10*digit+int(s[i])
            elif cur_op=='+':
                res+=digit
                prev=digit
                digit=0
                cur_op=s[i]
            elif cur_op=='-':
                res-=digit
                prev=-digit
                digit=0
                cur_op=s[i]
            elif cur_op=='*':
                res-=prev
                res+=(prev*digit)
                prev=(prev*digit)
                digit=0
                cur_op=s[i]
            elif cur_op=='/':
                res-=prev
                res+=int(prev/digit)
                prev=int(prev/digit)
                digit=0
                cur_op=s[i]
            i+=1
        return res
