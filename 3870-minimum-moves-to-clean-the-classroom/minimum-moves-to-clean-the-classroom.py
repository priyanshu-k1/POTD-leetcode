from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start = None
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        if num_litters == 0:
            return 0
            
        target_mask = (1 << num_litters) - 1
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        visited = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        sr, sc = start
        queue = deque([(sr, sc, 0, energy)])
        visited[sr][sc][0] = energy
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c, mask, cur_e = queue.popleft()
                
                if mask == target_mask:
                    return steps
                    
                if cur_e == 0:
                    continue
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n:
                        cell = classroom[nr][nc]
                        if cell == 'X':
                            continue
                            
                        next_e = cur_e - 1
                        next_mask = mask
                        
                        if cell == 'L':
                            next_mask |= (1 << litter_map[(nr, nc)])
                        elif cell == 'R':
                            next_e = energy
                            
                        if next_e > visited[nr][nc][next_mask]:
                            visited[nr][nc][next_mask] = next_e
                            queue.append((nr, nc, next_mask, next_e))
            steps += 1
                            
        return -1