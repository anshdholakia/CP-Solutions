class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        minsums=[x+y for x, y in pairwise(weights)]
        maxsums=[-(x+y) for x, y in pairwise(weights)]
        heapq.heapify(minsums)
        heapq.heapify(maxsums)
        mintotal=weights[0]+weights[-1]
        maxtotal=weights[0]+weights[-1]
        for _ in range(k-1):
            mintotal+=heapq.heappop(minsums)
            maxtotal+=-heapq.heappop(maxsums)
        return maxtotal-mintotal
        
