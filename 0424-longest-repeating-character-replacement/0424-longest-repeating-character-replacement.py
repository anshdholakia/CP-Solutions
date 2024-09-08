class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        current_map = {}
        current_max = 0
        result = 0
        for r in range(len(s)):
            current_map[s[r]] = current_map.get(s[r], 0) + 1
            current_max = max(current_max, current_map[s[r]])
            while r-l+1-current_max>k:
                current_map[s[l]]-=1
                l+=1
            result = max(result, r-l+1)
        return result