class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products=defaultdict(int)
        groups=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                groups+=products[nums[i]*nums[j]]
                products[nums[i]*nums[j]]+=1
        return 8*groups