class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        fact, cost = zip(*items)
        have = [0] * (max(fact) + 1)

        for factor in fact:
            have[factor] += 1

        gains = {factor: sum(have[factor::factor]) for factor in set(fact)} 
        cheapest = min(cost)

        sol = [cash // cheapest for cash in range(budget + 1)]
        for factor, price in items:
            if (gain := gains[factor]) > price // cheapest:
                for cash in range(budget, price - 1, -1):
                    sol[cash] = max(sol[cash], sol[cash - price] + gain)

        return sol[budget]
        