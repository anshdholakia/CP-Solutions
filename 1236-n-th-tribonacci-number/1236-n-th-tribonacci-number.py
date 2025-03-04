class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n<3:
            return [0,1,1][n]
        for i in range(4, n+1):
            temp=c
            c=a+b+c
            b, a=temp, b
        return a+b+c