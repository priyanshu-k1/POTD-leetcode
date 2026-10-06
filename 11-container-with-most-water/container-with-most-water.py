class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            maxHeight = min(height[left],height[right])
            distance = right - left
            maxArea = max(maxArea,maxHeight*distance)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1      
        return maxArea
        