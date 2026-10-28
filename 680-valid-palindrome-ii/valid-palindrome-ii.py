class Solution:
    def isPalindrome(self,s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        while l < r :
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
        return True
        