class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        depth = 0
        if len(s) == 0:
            return res
        for i in s:
            if i == "(":
                if  depth > 0:
                    res+= i 
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res += i        
        return res
        