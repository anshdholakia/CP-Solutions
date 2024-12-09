class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result=[False]*len(queries)
        queries=[[t[0], t[1], i] for i, t in enumerate(queries)]
        queries.sort(key=lambda x: (x[0], x[1]))
        # minheap stores end, index of query
        minheap=[]
        idx=0
        latest_hiccup=None
        for i in range(len(nums)):
            while idx<len(queries) and queries[idx][0]==i:
                heapq.heappush(minheap, (queries[idx][1], queries[idx][0], queries[idx][2]))
                idx+=1
            while minheap and minheap[0][0]==i:
                pope, pops, popi = heapq.heappop(minheap)
                if latest_hiccup!=None:
                    result[popi] = pops<=latest_hiccup<=pope
            if i+1<len(nums) and ((nums[i]%2 and nums[i+1]%2) or (nums[i]%2==0 and nums[i+1]%2==0)):
                latest_hiccup=i
        return [not x for x in result]