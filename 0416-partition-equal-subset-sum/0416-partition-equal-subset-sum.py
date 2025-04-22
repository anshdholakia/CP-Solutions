class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # get the possible sums in the array
        total=sum(nums)
        if total%2:
            return False
        half = total//2
        sums=set({0})
        for n in nums:
            for s in sums.copy():
                sums.add(n+s)
                if half in sums:
                    return True
        return False