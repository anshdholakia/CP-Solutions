class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # bottom up dp
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                    dungeon[i][j] = 0 if dungeon[i][j]>=0 else dungeon[i][j]
                else:
                    dungeon[i][j]+=max(min(0, dungeon[i+1][j]) if i+1<len(dungeon) else -inf, min(0, dungeon[i][j+1]) if j+1<len(dungeon[0]) else -inf)
        return abs(min(0, dungeon[0][0]))+1