class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        l = 0
        cur_count = {}
        result = []
        for r in range(len(s)):
            if s[r] in target:
                if not cur_count:
                    l=r
                cur_count[s[r]] = cur_count.get(s[r], 0) + 1
                while cur_count[s[r]]>target[s[r]]:
                    cur_count[s[l]]-=1
                    l+=1
                if cur_count==target:
                    result.append(l)
            else:
                cur_count = {}
        return result