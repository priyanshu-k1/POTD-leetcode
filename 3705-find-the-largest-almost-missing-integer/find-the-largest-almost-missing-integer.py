from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            counts = Counter(nums)
            valid = [num for num, freq in counts.items() if freq == 1]
            return max(valid) if valid else -1
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
        return ans
        