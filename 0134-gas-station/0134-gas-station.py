class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        diff=[g-c for g, c in zip(gas, cost)]
        idx=0
        curs=0
        for i in range(len(diff)-1, -1, -1):
            curs+=diff[i]
            if curs>0:
                idx=i
                curs=0
        return idx