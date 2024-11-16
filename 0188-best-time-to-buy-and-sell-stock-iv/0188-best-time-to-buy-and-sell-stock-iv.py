

class Solution:
    def f(self,ind,transNo,n,k,price,dp):
        if ind==n or transNo==2*k:
            return 0
        if dp[ind][transNo]!=-1:
            return dp[ind][transNo]
        if transNo%2==0:    #buy
            profit=max(-price[ind] + self.f(ind+1,transNo+1,n,k,price,dp),
                            0      + self.f(ind+1,transNo,n,k,price,dp))
        else:
            profit=max(price[ind] + self.f(ind+1,transNo+1,n,k,price,dp),
                            0     + self.f(ind+1,transNo,n,k,price,dp))
        dp[ind][transNo]= profit
        return dp[ind][transNo]
            
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for i in range(2*k)]for j in range(n)]
        return self.f(0,0,n,k,prices,dp)