class ProductOfNumbers:

    def __init__(self):
        self.ps={}
        self.cur_m=1
        self.length=0
        self.last_zero=None


    def add(self, num: int) -> None:
        self.ps[self.length]=self.cur_m
        self.length+=1
        if num!=0:
            self.cur_m*=num
        else:
            self.last_zero=self.length

    def getProduct(self, k: int) -> int:
        if self.last_zero and k>self.length-self.last_zero:
            return 0
        return int(self.cur_m/self.ps[self.length-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)