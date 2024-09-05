class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for c in range(len(s)):
            last_index[s[c]]=c
        result = []
        l, r = 0, 0
        for i in range(len(s)):
            r=max(r, last_index[s[i]])
            if i==r:
                result.append(r-l+1)
                l=r+1
        return result
