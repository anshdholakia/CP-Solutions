# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # eliminate each of the celebrities
        top, bottom = 0, n-1
        while top!=bottom:
            if knows(top, bottom):
                top+=1
            else:
                bottom-=1
        # check if the guy is actually a celebrity or not
        # check row and column
        count=0
        for i in range(n):
            if knows(i, top):
                count+=1
        for i in range(n):
            if i!=top and knows(top, i):
                return -1
        return top if count==n else -1