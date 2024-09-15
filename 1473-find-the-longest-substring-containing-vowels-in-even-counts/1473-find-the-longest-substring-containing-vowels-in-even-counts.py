class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix = {0:-1}
        cur_count = 00000 #'aeiou' one bit for one vowel
        result = 0
        idx = None
        for i in range(len(s)):
            if s[i] in 'aeiou':
                idx = 'aeiou'.index(s[i])
                cur_count ^= (1<<idx)
            if cur_count in prefix:
                result=max(result, i-prefix[cur_count])
            else:
                prefix[cur_count]=i
        return result
