class Solution:
    def trap(self, height: list[int]) -> int:
        left = water = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            if leftMax < rightMax :
                left += 1
                leftMax = max(leftMax,height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax,height[right])
                water += rightMax - height[right]
        return water
        