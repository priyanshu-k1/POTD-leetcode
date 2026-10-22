class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        if len(s) == 0:
            return True
        for ch in t:
            if len(s) == 0:
                break
            if ch == s[0]:
                s.pop(0)
        return True if len(s) == 0 else False
        