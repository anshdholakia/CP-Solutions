class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return list(set([k for k, v in collections.Counter((s1+" "+s2).split(" ")).items() if v==1]))