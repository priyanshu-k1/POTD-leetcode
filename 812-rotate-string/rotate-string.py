class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s * 2
        if goal in s:
            return True
        return False
        