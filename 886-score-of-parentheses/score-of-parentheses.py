class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for i in s:
            if i == "(":
                stk.append(0)
            elif i ==")" and len(stk) != 0:
                inner = stk.pop()
                if inner == 0:
                    stk[-1] += 1
                else:
                    stk[-1] += 2 * inner
        return stk[0]
        