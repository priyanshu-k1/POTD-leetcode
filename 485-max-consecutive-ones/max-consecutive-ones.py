class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxOnes = 0
        currMax = 0
        for num in nums:
            if num == 1:
                currMax += 1
            else:
                currMax = 0
            maxOnes = max(maxOnes,currMax)
        return maxOnes
        