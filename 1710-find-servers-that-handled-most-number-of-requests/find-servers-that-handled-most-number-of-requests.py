class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        avlServers = SortedList(range(k))
        busy = []
        cnt = [0] * k
        for reqId, (arrTime, pTime) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arrTime:
                endTime, serverId = heappop(busy)
                avlServers.add(serverId)
            if not avlServers:
                continue
            target = reqId % k
            idx = avlServers.bisect_left(target)
            if idx == len(avlServers):
                idx = 0
            server = avlServers[idx]
            cnt[server] += 1
            heappush(busy, (arrTime + pTime, server))
            avlServers.remove(server)
        maxReq = max(cnt)
        return [serverId for serverId, count in enumerate(cnt) if count == maxReq]
        