class MyHashMap:

    def __init__(self):
        self.n=10000
        self.listt=[[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        idx=key%self.n
        # check if it already exists
        for i, (k, val) in enumerate(self.listt[idx]):
            if k==key:
                self.listt[idx][i][1]=value
                break
        else:
            self.listt[idx].append([key, value])

    def get(self, key: int) -> int:
        idx=key%self.n
        # check if it already exists
        for i, (k, val) in enumerate(self.listt[idx]):
            if k==key:
                return val
        return -1

    def remove(self, key: int) -> None:
        idx=key%self.n
        # check if it already exists
        for i, (k, val) in enumerate(self.listt[idx]):
            if k==key:
                self.listt[idx].pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)