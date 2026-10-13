class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]**2
        nums.sort(reverse=True)
        mid = n // 2 if n%2 != 0 else (n // 2)-1
        score = 0
        for i in range(n):
            if i <= mid:
                score +=nums[i]
            else:
                score -= nums[i]
        return score