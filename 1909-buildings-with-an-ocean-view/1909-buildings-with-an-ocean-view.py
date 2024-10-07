class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_h = float("-inf")
        for i in range(len(heights)-1, -1, -1):
            if heights[i]>max_h:
                result.append(i)
            max_h = max(max_h, heights[i])
        return result[::-1]