class Solution:
    def minimumSteps(self, s: str) -> int:
        blackc = 0
        swaps = 0
        for i in range(len(s)):
            if s[i]=='0':
                if i!=blackc:
                    swaps+=(i-blackc)
                blackc+=1
        return swaps
