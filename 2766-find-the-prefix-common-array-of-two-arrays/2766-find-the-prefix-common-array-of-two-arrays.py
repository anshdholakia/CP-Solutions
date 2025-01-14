class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        final=[]
        a_set, b_set = set({}), set({})
        for a, b in zip(A, B):
            a_set.add(a)
            b_set.add(b)
            final.append(len(a_set.intersection(b_set)))
        return final