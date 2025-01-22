class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue=collections.deque([])
        visited=set({})
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    isWater[i][j]=0
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in pairwise([-1,0,1,0,-1]):
                    if 0<=x+dx<len(isWater) and 0<=y+dy<len(isWater[0]) and (x+dx, y+dy) not in visited:
                        visited.add((x+dx, y+dy))
                        isWater[x+dx][y+dy]=isWater[x][y]+1
                        queue.append((x+dx, y+dy))
        return isWater

