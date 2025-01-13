class Solution:
    def minimumLength(self, s: str) -> int:
        count=collections.Counter(s)
        result=0
        for v in count.values():
            if v%2:
                result+=1
            else:
                result+=2
        return result