class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur_xor=0
        res=[]
        for n in nums:
            cur_xor^=n
            # flip the bits to get max BUT only do after maxbit
            mask=(1<<maximumBit)-1
            res.append(cur_xor^mask)
        return res[::-1]