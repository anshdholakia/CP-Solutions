class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum([set(allowed).intersection((sett:=set(w)))==sett for w in words])