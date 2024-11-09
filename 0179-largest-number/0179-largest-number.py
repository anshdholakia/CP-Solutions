class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str, nums))
        def cmp(n1, n2):
            if n2+n1>n1+n2:
                return 1
            return -1
        nums.sort(key=cmp_to_key(cmp))
        return str(int("".join(nums)))