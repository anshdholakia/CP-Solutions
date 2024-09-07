class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = collections.Counter(s)
        left = set({})
        res=set({})
        for m in range(0, len(s)-1):
            right[s[m]]-=1
            if right[s[m]]==0:
                del right[s[m]]
            for lw in left:
                if lw in right:
                    res.add((s[m], lw))
            left.add(s[m])
        return len(res)
