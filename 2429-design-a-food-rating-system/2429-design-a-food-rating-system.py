from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_max = defaultdict(SortedSet)
        self.cuisine_map = {} # food -> cuisine
        self.rating_map = {} # food -> rating
        for f, c, r in zip(foods, cuisines, ratings):
            self.cuisine_max[c].add((-r, f))
            self.cuisine_map[f] = c
            self.rating_map[f] = r

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisine_map[food]
        r = self.rating_map[food]
        self.cuisine_max[c].remove((-r, food))
        self.cuisine_max[c].add((-newRating, food))
        self.rating_map[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_max[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)