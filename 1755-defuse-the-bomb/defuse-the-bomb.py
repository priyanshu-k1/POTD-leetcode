class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        output = [0]*n
        if k == 0:
            return output
        for i in range(n):
            for offset in range(1,abs(k)+1):
                idx = ((i - offset) if k < 0 else (i + offset)) % n
                output[i] += code[idx]
        return output
        