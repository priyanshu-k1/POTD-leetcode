class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        onceImg1 = []
        onceImg2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    onceImg1.append((i, j))
                if img2[i][j] == 1:
                    onceImg2.append((i, j))
        count = Counter()
        for (x1, y1) in onceImg1:
            for (x2, y2) in onceImg2:
                shift = (x2 - x1, y2 - y1)
                count[shift] += 1
        return max(count.values() or [0])
            