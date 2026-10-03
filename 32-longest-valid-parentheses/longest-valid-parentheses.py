class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 1:
            return 0
        stk = [-1]
        maxCnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()

                if len(stk) == 0:
                    stk.append(i)
                else:
                    currCnt = i - stk[-1]
                    maxCnt = max(maxCnt, currCnt)
        return maxCnt
            