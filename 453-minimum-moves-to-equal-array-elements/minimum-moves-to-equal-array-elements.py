class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        minElement = min(nums)
        moves = 0
        for i in nums:
            moves += (minElement - i)
        return abs(moves)
        