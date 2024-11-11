class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window with only 2 unique fruits
        fruit={}
        l=0
        res=0
        for r in range(len(fruits)):
            fruit[fruits[r]]=fruit.get(fruits[r],0)+1
            while len(fruit)>2:
                fruit[fruits[l]]-=1
                if fruit[fruits[l]]==0:
                    del fruit[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res
