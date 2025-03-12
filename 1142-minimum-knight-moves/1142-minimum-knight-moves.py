class Solution:
    def minKnightMoves(self, x_t: int, y_t: int) -> int:
        # since x and y can be from ranges -300 to 300
        # use bfs level by level to find it
        queue=collections.deque([(0, 0)])
        visited=set({(0, 0)})
        level=0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x==x_t and y==y_t:
                    return level
                for dirx, diry in [(-2, 1), (1, -2), (2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (-1, -2)]:
                    if -300<=x+dirx<=300 and -300<=y+diry<=300 and (x+dirx, y+diry) not in visited:
                        visited.add((x+dirx, y+diry))
                        queue.append((x+dirx, y+diry))
            level+=1
