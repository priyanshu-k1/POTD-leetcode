class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for i in s:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        for i in t:
            if i in mp and mp[i] != 0:
                mp[i] -=1
            else:
                return False
        return True
        