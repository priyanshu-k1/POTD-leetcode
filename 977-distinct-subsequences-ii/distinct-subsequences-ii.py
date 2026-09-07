class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * 26 for _ in range(n + 1)]
        for i, char in enumerate(s, 1):
            char_index = ord(char) - ord('a')
            for j in range(26):
                if j == char_index:
                    dp[i][j] = (sum(dp[i - 1]) % MOD + 1) % MOD
                else:
                    dp[i][j] = dp[i - 1][j]
        return sum(dp[-1]) % MOD
