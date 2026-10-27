class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        pPTR = 0
        tPTR = 0
        cnt = 0

        while pPTR < len(players) and tPTR < len(trainers):
            if players[pPTR] <= trainers[tPTR]:
                cnt += 1
                pPTR += 1
                tPTR += 1
            else:
                tPTR += 1
        return cnt
                
