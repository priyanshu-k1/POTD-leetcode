class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stk = []
        cnt = 0
        for i in s:
            if i == "(":
                stk.append(i)
            elif i == ")" and len(stk) != 0:
                stk.pop()
            else:
                cnt += 1
        return cnt + len(stk)

        