class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxEl = max(nums)
        moves = 0
        for i in nums:
            moves += (maxEl - i)
        return moves
        