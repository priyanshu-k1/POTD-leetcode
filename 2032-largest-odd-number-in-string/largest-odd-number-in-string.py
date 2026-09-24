class Solution:
    def largestOddNumber(self, num: str) -> str:
        ptr = len(num) -1
        while ptr>=0 and int(num[ptr])%2 ==0:
            ptr -= 1
        return num[0:ptr+1]
            
        