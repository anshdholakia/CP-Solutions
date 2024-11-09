class Solution:
    def candy(self, ratings: List[int]) -> int:
        c=[1]*len(ratings)
        for i in range(1, len(ratings)):
            # look at the left guy here
            if ratings[i-1]<ratings[i] and c[i]<=c[i-1]:
                c[i]=c[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            # look at the right guy here
            if ratings[i+1]<ratings[i] and c[i]<=c[i+1]:
                c[i]=c[i+1]+1
        return sum(c)
