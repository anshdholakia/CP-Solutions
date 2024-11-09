class RandomizedSet:

    def __init__(self):
        self.valToIdx={} # value to index
        self.nums=[]
        self.cur_length=0

    def insert(self, val: int) -> bool:
        if val in self.valToIdx:
            return False
        self.valToIdx[val]=self.cur_length
        if self.cur_length==len(self.nums):
            self.nums.append(val)
        else:
            self.nums[self.cur_length]=val
        self.cur_length+=1
        return True

    def remove(self, val: int) -> bool:
        if val in self.valToIdx:
            # swap the last element of the array with removed
            idx=self.valToIdx[val]
            self.nums[idx], self.nums[self.cur_length-1] = self.nums[self.cur_length-1], self.nums[idx]
            self.valToIdx[self.nums[idx]]=idx
            self.cur_length-=1
            del self.valToIdx[val]
            return True
        return False
    def getRandom(self) -> int:
        return self.nums[random.randint(0, self.cur_length-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()