class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # do bfs from gates
        queue=collections.deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    queue.append((i, j))
        visited=set({})
        INF=2147483647
        levels=0
        while queue:
            levels+=1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in pairwise([-1,0,1,0,-1]):
                    if 0<=dx+x<len(rooms) and 0<=dy+y<len(rooms[0]) and rooms[x+dx][y+dy]==INF and (x+dx, y+dy) not in visited:
                        rooms[x+dx][y+dy]=levels
                        visited.add((x+dx, y+dy))
                        queue.append((x+dx, y+dy))
