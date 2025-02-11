class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tt=[((target-p)/s, p) for p, s in zip(position, speed)]
        tt.sort(key=lambda x: x[1], reverse=True)
        stack=[]
        for time, pos in tt:
            while stack and stack[-1]>=time:
                time=stack.pop()
            stack.append(time)
        return len(stack)