class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # keep num2 as the smaller string
        if len(num1)<len(num2): 
            num1, num2 = num2, num1
        num1=num1[::-1]
        num2=num2[::-1]
        carry=0
        res=""
        i, j = 0, 0
        while j<len(num2):
            digit=carry+int(num1[i])+int(num2[j])
            if digit//10:
                carry=digit//10
            else:
                carry=0
            res+=str(digit%10)
            i+=1
            j+=1
        while i<len(num1):
            digit=carry+int(num1[i])
            if digit//10:
                carry=digit//10
            else:
                carry=0
            res+=str(digit%10)
            i+=1
        if carry:
            res+=str(carry)
        return res[::-1]
