class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start, goal = bin(start).split("b")[1], bin(goal).split("b")[1]
        start, goal = start.zfill(max(len(start), len(goal))), goal.zfill(max(len(start), len(goal)))
        return sum([1 if i!=j else 0 for i, j in zip(start, goal)])

