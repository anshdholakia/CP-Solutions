class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
        # use a monotonic stack
        stack=[]
        for n in num:
            while k and (stack and stack[-1]>n):
                stack.pop()
                k-=1
            stack.append(n)
        # remove the last few
        stack=stack[:len(stack)-k]
        res="".join(stack)
        res=res.lstrip("0")
        return res if res else "0"

        