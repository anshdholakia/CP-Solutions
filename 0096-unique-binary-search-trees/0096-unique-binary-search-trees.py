class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1]*(n+1)
        for nodes in range(2, n+1):
            total=0
            for root in range(nodes):
                left=root
                right=nodes-root-1
                total+=(dp[left]*dp[right])
            dp[nodes]=total
        return dp[-1]