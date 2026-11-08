class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    canCommunicate = False
                    for otherCol in range(cols):
                        if otherCol != col and grid[row][otherCol] == 1:
                            canCommunicate = True
                            break
                    if canCommunicate:
                        cnt += 1
                    else:
                        for otherRow in range(rows):
                            if otherRow != row and grid[otherRow][col] == 1:
                                canCommunicate = True
                                break
                        if canCommunicate:
                            cnt += 1
        return cnt