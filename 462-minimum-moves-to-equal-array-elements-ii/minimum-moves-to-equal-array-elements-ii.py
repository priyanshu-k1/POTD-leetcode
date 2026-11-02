import numpy as np
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mdn = round(np.median(nums))
        moves = 0
        for i in nums:
            moves += abs(mdn - i)
        return moves
        