class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_res = float("-inf")
        heights.append(float("-inf"))
        stack = []
        for i, h in enumerate(heights):
            new_i=i
            while stack and stack[-1][-1]>h:
                popped = stack.pop()
                max_res = max(max_res, popped[1]*(i-popped[0]))
                new_i=popped[0]
            stack.append((new_i, h))
        return max_res