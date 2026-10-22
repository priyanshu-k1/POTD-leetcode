class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        tPtr = 0
        nS = len(s)
        nT = len(t)
        while tPtr < nT and sPtr < nS:
            if s[sPtr] == t[tPtr]:
                sPtr +=1
                tPtr +=1
            else:
                tPtr +=1
        return True if sPtr >= nS else False
        