class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count=[0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        for _ in range(t):
            dummy=count.copy()
            prev=dummy[-1]
            for i in range(len(dummy)-2, -1, -1):
                dummy[i+1]=dummy[i]
            dummy[0]=prev
            dummy[1]+=prev
            count=dummy
        return sum(count)%(10**9+7)