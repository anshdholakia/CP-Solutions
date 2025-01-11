class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count=collections.Counter(s)
        odd=0
        for v in count.values():
            if v%2:
                odd+=1
        return odd<=k and k<=len(s)