class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        left = 0
        right = n-1
        vovels = {"A","E","I","O","U","a","e","i","o","u"}
        while left < right:
            if s[left] in vovels and s[right] in vovels:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            if s[left] not in vovels:
                left += 1
            if s[right] not in vovels:
                right -= 1
        return "".join(s)
        