class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        res=0
        curs=0
        for i in range(1, n+1):
            if i not in banned:
                curs+=i
                res+=1
            if curs>maxSum:
                return res-1
        return res