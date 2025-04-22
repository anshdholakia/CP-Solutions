class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            temp=b
            b=min(cost[i]+a, cost[i]+b)
            a=temp
        return min(a, b)