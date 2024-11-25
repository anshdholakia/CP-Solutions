class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1, count2 = collections.Counter(s), collections.Counter(t)
        # get rid of count which are already there
        for c in count1:
            count2[c]=max(0, count2.get(c,0)-count1[c])
        return sum(count2.values())