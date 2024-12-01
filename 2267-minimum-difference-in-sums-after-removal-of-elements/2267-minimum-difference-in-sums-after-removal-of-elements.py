class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # build a prefix and suffix array
        # the prefix array is built using heap which basically means the prefix at a position in the array which is minimum
        N = len(nums)/3
        prefix, suffix=[], []
        minheap, maxheap = [], []
        curs=0
        for i, x in enumerate(nums):
            curs+=x
            heapq.heappush(maxheap, -x)
            if len(maxheap)>N:
                curs+=heapq.heappop(maxheap)
            if len(maxheap)==N:
                prefix.append(curs)
            else:
                prefix.append(inf)
        curs=0
        for i, x in enumerate(reversed(nums)):
            curs+=x
            heapq.heappush(minheap, x)
            if len(minheap)>N:
                curs-=heapq.heappop(minheap)
            if len(minheap)==N:
                suffix.append(curs)
            else:
                suffix.append(inf)
        suffix=suffix[::-1]
        ans=inf
        for i in range(len(suffix)-1):
            if prefix[i]!=inf and suffix[i+1]!=inf:
                ans=min(ans, prefix[i]-suffix[i+1])
        return ans

        # the suffix array is built using minheap which basicaly means the suffix at a position in the array which is maximum

        