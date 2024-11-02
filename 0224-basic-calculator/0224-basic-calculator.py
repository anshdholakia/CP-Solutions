class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        s=s.replace(" ", "")
        s=f'({s})'
        for i, c in enumerate(s):
            if c==')':
                ev=[]
                while stack[-1]!='(':
                    ev.append(stack.pop())
                ev="".join(ev[::-1]).replace("--","+")
                stack.pop()
                # evaluate ev and push back to stack
                res=0
                cur_digit=0
                cur_op='+'
                for i in range(len(ev)):
                    if not ev[i].isdigit():
                        if cur_op=='+':
                            res+=cur_digit
                        else:
                            res-=cur_digit
                        cur_op=ev[i]
                        cur_digit=0
                    else:
                        cur_digit=(cur_digit*10)+int(ev[i])
                if cur_op=='+':
                    res+=cur_digit
                else:
                    res-=cur_digit
                stack.append(str(res))
            else:
                stack.append(c)
        return int(stack[0])
