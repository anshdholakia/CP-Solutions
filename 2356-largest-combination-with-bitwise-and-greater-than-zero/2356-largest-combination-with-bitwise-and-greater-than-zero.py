class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count=[0]*32
        for c in candidates:
            idx=0
            while c:
                if c&1:
                    count[idx]+=1
                idx+=1
                c=(c>>1)
        return max(count)