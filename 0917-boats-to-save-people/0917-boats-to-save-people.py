class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                boats+=1
                l+=1
                r-=1
            else:
                boats+=1
                r-=1
        return boats