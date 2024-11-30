class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMax, rightMax = height[0], height[-1]
        res=0
        while left<right:
            if leftMax<rightMax:
                res+=leftMax-height[left]
                left+=1
                leftMax=max(leftMax, height[left])
            else:
                res+=rightMax-height[right]
                right-=1
                rightMax=max(rightMax, height[right])
        return res