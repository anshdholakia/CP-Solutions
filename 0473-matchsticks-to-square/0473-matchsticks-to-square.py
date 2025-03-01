class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total%4:
            return False
        side=total//4
        sides=[0]*4
        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i]<=side:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return backtrack(0)