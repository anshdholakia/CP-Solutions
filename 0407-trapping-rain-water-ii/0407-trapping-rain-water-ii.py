class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        minheap=[]
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i in [0, len(heightMap)-1] or j in [0, len(heightMap[0])-1]:
                    heapq.heappush(minheap, (heightMap[i][j], i, j))
                    heightMap[i][j]=-1 # mark visited
        maxh=-1
        res=0
        while minheap:
            h, r, c = heapq.heappop(minheap)
            maxh=max(maxh, h)
            res+=(maxh-h)
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=dx+r<len(heightMap) and 0<=c+dy<len(heightMap[0]) and heightMap[dx+r][dy+c]!=-1:
                    heapq.heappush(minheap, (heightMap[dx+r][dy+c],dx+r, dy+c))
                    heightMap[dx+r][dy+c]=-1
        return res
