class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        asc = sorted(people)
        l, r = 0, len(asc)-1
        boats = 0
        while l<=r:
            if asc[l]+asc[r]>limit:
                r-=1
            else:
                l+=1
                r-=1
            boats+=1
        return boats
