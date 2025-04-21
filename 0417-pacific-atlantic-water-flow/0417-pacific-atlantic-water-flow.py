class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic=set({})
        pacific=set({})
        def dfs(i, j, hashset):
            hashset.add((i, j))
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+i<len(heights) and 0<=dy+j<len(heights[0]) and (dx+i, dy+j) not in hashset and heights[dx+i][dy+j]>=heights[i][j]:
                    dfs(dx+i,dy+j,hashset)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0:
                    dfs(i, j, pacific)
                if i==len(heights)-1 or j==len(heights[0])-1:
                    dfs(i, j, atlantic)
        return list(atlantic.intersection(pacific))