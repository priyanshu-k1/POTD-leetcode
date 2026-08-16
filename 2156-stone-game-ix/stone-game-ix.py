class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def aliceWin(count: list[int]) -> bool:
            if count[1] == 0:
                return False
            count[1] -= 1
            total_moves = 1 + min(count[1], count[2]) * 2 + count[0]
            if count[1] > count[2]:
                count[1] -= 1
                total_moves += 1
            return total_moves % 2 == 1 and count[1] != count[2]
        remCount = [0] * 3
        for stone in stones:
            remCount[stone % 3] += 1
        strategy_one = [remCount[0], remCount[1], remCount[2]]
        strategy_two = [remCount[0], remCount[2], remCount[1]]
        return aliceWin(strategy_one) or aliceWin(strategy_two)
        