class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # build two arrays, one to store max value till now
        # and one to store the ending values of the intervals
        ends, maxs = [], []
        max_now=0
        result=0
        for s, e, v in sorted(events, key=lambda x: x[1]):
            max_now=max(max_now, v)
            # binary search for the events before this start time
            l, r = 0, len(ends)-1
            res=None
            while l<=r:
                m=(l+r)//2
                if ends[m]<s:
                    res=m
                    l=m+1
                else:
                    r=m-1
            result=max(result, v)
            if res!=None:
                result=max(result, v+maxs[res])
            ends.append(e)
            maxs.append(max_now)
        return result