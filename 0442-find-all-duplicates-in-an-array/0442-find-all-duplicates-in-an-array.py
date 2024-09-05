class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [n for n, v in collections.Counter(nums).items() if v==2]