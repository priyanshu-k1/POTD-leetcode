class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        low = 0
        mid = low
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
        
        