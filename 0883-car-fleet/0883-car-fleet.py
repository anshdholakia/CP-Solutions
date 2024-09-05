class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken = sorted([(p, (target-p)/s) for p, s in zip(position, speed)])
        stack = []
        for pos, time in time_taken:
            while stack and stack[-1][-1]<=time:
                stack.pop()
            stack.append((pos, time))
        return len(stack)
