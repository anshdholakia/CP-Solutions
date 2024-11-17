class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count=collections.Counter(citations)
        csum=len(citations)
        res=0
        for i in range(max(citations)+1):
            if csum>=i:
                res=i
            csum-=count.get(i, 0)
        return res
