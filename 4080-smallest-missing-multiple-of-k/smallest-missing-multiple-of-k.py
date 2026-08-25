class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        lookup = set(nums)
        if k not in lookup:
            return k 
        i = k
        while(True):
            if i % k ==0 and i not in lookup:
                return i 
            i = i + k