class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        possible_sums=set({0})
        if total%2:
            return False
        for n in nums:
            for s in possible_sums.copy():
                possible_sums.add(s+n)
                if total//2 in possible_sums:
                    return True
        return False