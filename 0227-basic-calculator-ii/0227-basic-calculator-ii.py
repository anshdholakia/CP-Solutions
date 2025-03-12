class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")+'+'
        cur_op='+'
        idx=0
        digit=0
        prev_digit=0
        result=0
        while idx<len(s):
            if s[idx].isdigit():
                digit=digit*10+int(s[idx])
            else:
                if cur_op=='+':
                    prev_digit=digit
                    result+=digit
                elif cur_op=='-':
                    prev_digit=-digit
                    result-=digit
                elif cur_op=='*':
                    result-=prev_digit
                    prev_digit=prev_digit*digit
                    result+=prev_digit
                else:
                    result-=prev_digit
                    prev_digit=int(prev_digit/digit)
                    result+=prev_digit
                digit=0
                cur_op=s[idx]
            idx+=1
        return result