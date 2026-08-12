class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        counter  = {}
        for right in range(len(nums)):
            if nums[right] not in counter:
                counter[nums[right]] = 1
            else:
                counter[nums[right]] += 1
            while(counter[nums[right]] > k):
                counter[nums[left]] -= 1
                left += 1
            result = max(result,(right - left + 1))
        return result