class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort(reverse=True)
        # go through nums and check if the numbers have the same prefix and length if diff
        for i, j in zip(range(len(keys)-1), range(1, len(keys))):
            while i>=0 and j>=0 and keys[i].startswith(keys[j]) and len(keys[i])>len(keys[j]) and keys[j]+keys[i]>keys[i]+keys[j]:
                keys[j], keys[i] = keys[i], keys[j]
                i-=1
                j-=1
        result = []
        for k in keys:
            result = result + ([k]*count[k])
        return str(int("".join(result)))
        