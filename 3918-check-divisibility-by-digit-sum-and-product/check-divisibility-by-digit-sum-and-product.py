class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        prod = 1
        temp = n 
        while n != 0:
            digit = n % 10 
            sum += digit
            prod *= digit
            n //= 10
        if temp % (sum+prod) == 0 :
            return True
        return False
        
        