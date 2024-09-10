class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set({}), set({})
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0:
                    pacific.add((i, j))
                if i==len(heights)-1 or j==len(heights[0])-1:
                    atlantic.add((i, j))
        def dfs(x, y, mapping):
            queue = collections.deque([(x, y)])
            while queue:
                popx, popy = queue.popleft()
                for dirx, diry in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if popx+dirx>=0 and popx+dirx<len(heights) and popy+diry>=0 and popy+diry<len(heights[0]) and (popx+dirx, popy+diry) not in mapping and heights[popx+dirx][popy+diry]>=heights[popx][popy]:
                        queue.append((popx+dirx, popy+diry))
                        mapping.add((popx+dirx, popy+diry))
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0:
                    dfs(i, j, pacific)
                if i==len(heights)-1 or j==len(heights[0])-1:
                    dfs(i, j, atlantic)
        return list(pacific.intersection(atlantic))