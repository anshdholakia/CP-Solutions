class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            append=True
            while stack and stack[-1]>0 and a<0:
                if abs(stack[-1])>abs(a):
                    append=False
                    break
                elif abs(stack[-1])==abs(a):
                    append=False
                    stack.pop()
                    break
                stack.pop()
            if append:
                stack.append(a)
        return stack
