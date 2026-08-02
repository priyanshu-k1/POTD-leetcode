class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def solve(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return piles[i]
            first = piles[i] + min(solve(i + 2, j), solve(i + 1, j - 1))
            last  = piles[j] + min(solve(i, j - 2), solve(i + 1, j - 1)) 
            return max(first,last)

        total_stones = sum(piles)
        alice_score = solve(0, len(piles) - 1)
        
        return alice_score > (total_stones - alice_score)