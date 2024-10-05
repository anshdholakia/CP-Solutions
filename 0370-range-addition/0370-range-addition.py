class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ps = defaultdict(int) # stores the starting index and ending index and what to add to the current sum to make it represen the value at the index
        for s, e, inc in updates:
            ps[s]+=inc
            ps[e+1]-=inc
        cur_sum = 0
        result = []
        for i in range(length):
            cur_sum+=ps[i]
            result.append(cur_sum)
        return result