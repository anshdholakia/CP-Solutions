class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        openb, closeb = 0,0
        for i in range(len(s)):
            if s[i]=='[':
                openb+=1
            else:
                closeb+=1
            if closeb>openb:
                swaps+=1
                closeb-=1
                openb+=1
        return swaps