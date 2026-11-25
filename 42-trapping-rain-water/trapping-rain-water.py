class Solution:
    def trap(self, height: list[int]) -> int:
        n= len(height)
        left = 0
        right = n - 1
        leftMax = height[left]
        rightMax = height[right]
        water = 0
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
        