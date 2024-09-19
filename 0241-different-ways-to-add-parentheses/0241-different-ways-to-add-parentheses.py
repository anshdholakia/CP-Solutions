class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        s_exp = []
        l = 0
        for i in range(len(expression)):
            if expression[i] in '+-*':
                s_exp.append(expression[l:i])
                s_exp.append(expression[i])
                l=i+1
        s_exp.append(expression[l:i+1])
        def dnc(cur_stack):
            if len(cur_stack)>1:
                result = []
                for i in range(len(cur_stack)):
                    if cur_stack[i] == '+':
                        res1=dnc(cur_stack[:i])
                        res2=dnc(cur_stack[i+1:])
                        for r1 in res1:
                            for r2 in res2:
                                result.append(r1+r2)
                    elif cur_stack[i]=='-':
                        res1=dnc(cur_stack[:i])
                        res2=dnc(cur_stack[i+1:])
                        for r1 in res1:
                            for r2 in res2:
                                result.append(r1-r2)
                    elif cur_stack[i]=='*':
                        res1=dnc(cur_stack[:i])
                        res2=dnc(cur_stack[i+1:])
                        for r1 in res1:
                            for r2 in res2:
                                result.append(r1*r2)
                return result
            else:
                return [int(cur_stack[0])]
        return dnc(s_exp)