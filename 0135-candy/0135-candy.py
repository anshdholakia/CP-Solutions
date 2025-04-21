class Solution:
    def candy(self, ratings: List[int]) -> int:
        res=[1]*len(ratings)
        for i in range(len(ratings)):
            if i>0 and ratings[i-1]<ratings[i] and res[i-1]>=res[i]:
                res[i]=res[i-1]+1
        for i in range(len(ratings)-1, -1, -1):
            if i<len(ratings)-1 and ratings[i+1]<ratings[i] and res[i+1]>=res[i]:
                res[i]=res[i+1]+1
        return sum(res)