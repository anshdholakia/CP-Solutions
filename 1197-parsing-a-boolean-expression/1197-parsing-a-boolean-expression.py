class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [] # stores the &| with the previous values
        for i in range(len(expression)):
            if expression[i]=='(' or expression[i]==',':
                continue
            elif expression[i]=='&' or expression[i]=='|' or expression=='!':
                stack.append(expression[i])
            elif expression[i]==')':
                # pop till you get an expression
                values = []
                while stack and stack[-1] not in '&|!':
                    values.append(stack[-1]=='t')
                    stack.pop()
                op = stack.pop()
                if op=='&':
                    stack.append('t' if all(values) else 'f')
                elif op=='|':
                    stack.append('t' if any(values) else 'f')
                else:
                    stack.append('f' if values[0] else 't')
            else:
                stack.append(expression[i])
        return stack[0]=='t'
            
            


