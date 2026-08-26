class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
        min_length = float('inf')
        for start in range(n):
            ones_count = 0
            for end in range(start, n):
                if s[end] == '1':
                    ones_count += 1
                if ones_count == k:
                    current_length = end - start + 1
                    current_substring = s[start:end + 1]
                    if (current_length < min_length or 
                        (current_length == min_length and 
                         (not result or current_substring < result))):
                        result = current_substring
                        min_length = current_length
                    break  
                elif ones_count > k:
                    break
      
        return result