class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if collections.Counter(s1)!=collections.Counter(s2):
            return False
        if len(s1)==1: return True
        for k in range(1, len(s1)):
            if (self.isScramble(s1[:k], s2[-k:]) and self.isScramble(s1[k:], s2[:-k])) or (self.isScramble(s1[:k], s2[:k]) and self.isScramble(s1[k:], s2[k:])):
                return True
        return False