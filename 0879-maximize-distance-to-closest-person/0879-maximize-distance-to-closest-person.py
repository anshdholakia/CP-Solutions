class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0
        # look for result in start and end
        for i in range(len(seats)):
            if seats[i]:
                break
            result=max(result, i+1)
        for i in range(len(seats)-1, -1, -1):
            if seats[i]:
                break
            result=max(result, len(seats)-i)
        # find the maximum window size with two 1s
        person = False
        l = 0
        mid = 0
        for r in range(len(seats)):
            if seats[r]:
                if person:
                    mid = max(mid, r-l+1)
                l=r
                person=True
        if mid%2:
            return max(result, (mid-1)//2)
        else:
            return max(result, mid//2 - 1)
        