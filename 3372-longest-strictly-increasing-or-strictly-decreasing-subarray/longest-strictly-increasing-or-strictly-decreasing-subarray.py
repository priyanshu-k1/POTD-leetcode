class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        ascendingMaxLen = 1
        descendingMaxLen = 1
        maxLen = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                ascendingMaxLen += 1
                descendingMaxLen = 1
            elif nums[i] < nums[i-1]:
                descendingMaxLen += 1
                ascendingMaxLen = 1
            else:
                descendingMaxLen = ascendingMaxLen  = 1
            maxLen =  max(maxLen, ascendingMaxLen, descendingMaxLen)

        return maxLen
        