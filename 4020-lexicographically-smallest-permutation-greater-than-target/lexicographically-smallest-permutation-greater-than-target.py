class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        cur_counts = Counter(s)
        max_match = 0
        for char in target:
            if cur_counts[char] > 0:
                cur_counts[char] -= 1
                max_match += 1
            else:
                break
        for k in range(min(max_match, n - 1), -1, -1):
            remaining = total_counts.copy()
            for i in range(k):
                remaining[target[i]] -= 1
            target_ord = ord(target[k])
            for code in range(target_ord + 1, ord('z') + 1):
                char = chr(code)
                if remaining[char] > 0:
                    remaining[char] -= 1
                    suffix = "".join(sorted(remaining.elements()))
                    return target[:k] + char + suffix
                    
        return ""
        