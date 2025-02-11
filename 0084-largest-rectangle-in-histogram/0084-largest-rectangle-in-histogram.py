class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-inf)
        result=0
        stack=[]
        for i, h in enumerate(heights):
            idx=i
            while stack and stack[-1][1]>h:
                idx, height = stack.pop()
                result=max(result, height*(i-idx))
            stack.append((idx, h))
        return result