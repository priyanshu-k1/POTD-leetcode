class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        mx = nums[-1]
        dp = [0] * (mx + 2)
        ans = 1
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            ans = max(ans, dp[x], dp[x + 1])
        return ans