class Solution:
    def sumUP(self,n:int) -> int:
        total = 0
        while n:
            total += n%10
            n //= 10
        return total
    
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.sumUP(nums[i])  ==  i:
                return i
        return -1
            