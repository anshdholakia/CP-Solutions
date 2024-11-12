class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # do binary search between distance and the length of the position
        def allocate(minDist, k):
            k-=1
            prevPos=0
            for i in range(1, len(position)):
                if position[i]-position[prevPos]>=minDist:
                    prevPos=i
                    k-=1
                if k==0:
                    return True
            return False

        l, r = 1, position[-1]
        res=-inf
        while l<=r:
            mid=(l+r)//2
            if allocate(mid, m):
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res