class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,n):
            val = nums[i]
            dp[i+1] = max(dp[i],dp[i-1]+val)
        return dp[n]
        