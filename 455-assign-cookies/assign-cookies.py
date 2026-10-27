class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        gPTR = 0
        sPTR = 0
        cnt  = 0
        while gPTR < len(g) and sPTR < len(s):
            if g[gPTR] <= s[sPTR]:
                cnt +=1
                gPTR += 1
                sPTR += 1
            else:
                sPTR += 1
        return cnt 
        