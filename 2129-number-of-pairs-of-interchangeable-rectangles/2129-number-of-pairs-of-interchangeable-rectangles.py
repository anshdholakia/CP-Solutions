class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hash_map = defaultdict(int)
        for rec in rectangles:
            hash_map[rec[0]/rec[1]]+=1
        return int(sum([(n*(n-1))/2 for n in hash_map.values()]))