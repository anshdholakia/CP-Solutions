class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack=[]
        for n in nums:
            if not stack or n>stack[-1]:
                stack.append(n)
            else:
                idx=bisect_left(stack, n)
                stack[idx]=n
        return len(stack)