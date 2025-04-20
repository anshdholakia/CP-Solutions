class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[((target-p)/s, p) for s, p in zip(speed, position)]
        time.sort(key=lambda x:x[1])
        stack=[]
        for t, pos in time:
            while stack and stack[-1]<=t:
                stack.pop()
            stack.append(t)
        return len(stack)