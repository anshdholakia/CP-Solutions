class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        cur=[]
        def xor(array):
            current_xor=array[0] if array else 0
            for i in range(1, len(array)):
                current_xor^=array[i]
            return current_xor

        def backtrack(i):
            if i==len(nums):
                nonlocal result
                result+=xor(cur)
                return
            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()
            backtrack(i+1)
        backtrack(0)
        return result
