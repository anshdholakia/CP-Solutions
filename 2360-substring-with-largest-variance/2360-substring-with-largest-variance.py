class Solution:
    def largestVariance(self, s: str) -> int:
        pairs=[(s1, s2) for s1 in set(s) for s2 in set(s) if s1!=s2]
        ans=0
        for _ in range(2):
            for p in pairs:
                k1, k2 = 0, 0
                for c in s:
                    if c not in p:
                        continue
                    if c==p[0]:
                        k1+=1
                    elif c==p[1]:
                        k2+=1
                    if k2>k1:
                        k1, k2 = 0, 0
                    if k1>0 and k2>0:
                        ans=max(ans, abs(k1-k2))
            s=s[::-1]
        return ans