class Solution:
    def digitProd(self,n:int)->int:
        output = 1
        while n!=0:
            rem = n %10
            output *= rem
            n //= 10
        return output
    def smallestNumber(self, n: int, t: int) -> int:
        start = n
        while True:
            val = self.digitProd(start)
            if  val % t == 0:
                return start
            start += 1

        