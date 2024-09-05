class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        profit = []
        for i in range(len(gas)):
            profit.append(gas[i]-cost[i])
        if sum(profit)<0:
            return -1
        cursum = 0
        start = 0
        for i in range(len(profit)):
            cursum+=profit[i]
            if cursum<0:
                cursum=0
                start=i+1
        return start
            