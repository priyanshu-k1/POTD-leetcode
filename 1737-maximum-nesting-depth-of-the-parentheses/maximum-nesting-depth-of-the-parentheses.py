class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxCounter = 0
        for i in s:
            if i == "(":
                counter += 1
            if i == ")":
                counter -= 1
            maxCounter = max(maxCounter,counter)
        return maxCounter
            