class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minElement = min(nums)
        moves = 0
        for i in nums:
            moves += (i - minElement)
        return moves
        