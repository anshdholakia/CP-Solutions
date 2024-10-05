class Solution:
    def calculate(self, s: str) -> int:
        operation = '+'
        result = 0
        stack = []
        current = 0
        i = 0
        while i<len(s):
            if s[i].isdigit():
                current = current*10+int(s[i])
            if s[i] in '+-*/' or i==len(s)-1:
                if operation=='+':
                    stack.append(current)
                elif operation=='-':
                    stack.append(-current)
                elif operation=='*':
                    stack.append(stack.pop()*current)
                else:
                    stack.append(int(stack.pop()/current))
                operation=s[i]
                current=0
            i+=1
        return sum(stack)
