class Solution:
    def f(self,num,dp):
        if num == 1 or num == 0:
            return 1
        if dp[num] != -1:
            return dp[num]
        dp[num] = self.f(num - 1,dp) + self.f(num - 2,dp)
        return dp[num]
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.f(n,dp)
        