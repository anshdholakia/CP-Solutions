class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # use a maxheap to use bricks everytime but then use ladders when all bricks are used
        maxheap=[]
        idx=0
        while idx<len(heights)-1:
            if heights[idx]>heights[idx+1]:
                idx+=1
                continue
            # use bricks if positive
            bricks-=(heights[idx+1]-heights[idx])
            heapq.heappush(maxheap, -heights[idx+1]+heights[idx])
            if bricks<0:
                # check if we could use ladders for this
                if ladders:
                    ladders-=1
                    bricks-=heapq.heappop(maxheap)
                else:
                    break
            idx+=1
        return idx
