class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) else 1
        dividend, divisor=abs(dividend), abs(divisor)
        result=len(range(0,dividend-divisor+1,divisor))
        result=sign*result
        MAX=2**31-1
        MIN=-2**31
        return max(min(MAX, result), MIN)

