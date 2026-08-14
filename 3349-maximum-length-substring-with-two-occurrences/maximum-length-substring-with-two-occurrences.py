class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        res = 0
        counter = {}
        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]] = 1
            else:
                counter[s[right]] += 1
            while((counter[s[right]] > 2)):
                counter[s[left]] -= 1
                left += 1
            res = max(res,((right - left) +1))
        return res
            