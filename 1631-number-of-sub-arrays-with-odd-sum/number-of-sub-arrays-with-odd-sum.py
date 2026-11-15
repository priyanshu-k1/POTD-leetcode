class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1
        odd = 0
        cnt = prefix = 0
        for n in arr:
            prefix += n
            if prefix % 2 == 0:
                cnt += odd
                even += 1
            else:
                cnt += even
                odd += 1
        return (cnt % MOD)
        