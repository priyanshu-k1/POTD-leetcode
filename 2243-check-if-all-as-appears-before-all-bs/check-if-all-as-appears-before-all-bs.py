class Solution:
    def checkString(self, s: str) -> bool:
        lc = s[0]
        for ch in s[1:]:
            if ch == "a" and lc != "a":
                return False
            elif ch == "b" and (lc == "a" or lc == "b"):
                lc = "b"
        return True
        