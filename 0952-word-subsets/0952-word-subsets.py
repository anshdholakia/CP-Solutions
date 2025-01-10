class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # get max count of each character from words2
        count=collections.Counter()
        for word in words2:
            cur_count=collections.Counter(word)
            for c in cur_count:
                count[c]=max(count[c], cur_count[c])
        final=[]
        for word in words1:
            cur_count=collections.Counter(word)
            if all([cur_count[c]>=v for c, v in count.items()]):
                final.append(word)
        return final