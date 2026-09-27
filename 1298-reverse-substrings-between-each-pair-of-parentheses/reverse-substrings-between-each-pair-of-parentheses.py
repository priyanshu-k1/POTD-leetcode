class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp = []
        pairs = []
        if len(s) <= 1:
            return s
        s = [x for x in s]
        for i in range(len(s)):
            if s[i] == "(":
                temp.append((s[i],i)) 
            elif s[i] == ")" and len(temp) > 0:
                pairs.append((temp.pop()[1],i))
        for j in pairs:
            s[j[0]:j[1]] = s[j[0]:j[1]][::-1] 
        s = [x for x in s if x not in"()"]
        return "".join(s)
        