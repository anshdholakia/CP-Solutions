class RandomizedSet:

    def __init__(self):
        self.hashmap={}
        self.array=[]

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val]=len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx=self.hashmap[val]
        del self.hashmap[val]
        if idx!=len(self.array)-1:
            self.array[idx]=self.array[-1]
            self.hashmap[self.array[-1]]=idx
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()