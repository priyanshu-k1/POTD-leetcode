class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        winSum = 0
        freq = {}
        for j in range(k):
            winSum += nums[j]
            freq[nums[j]] = freq.get(nums[j], 0) + 1
        maxSum = winSum if len(freq) == k else 0
        for i in range(k,len(nums)):
            outgoing = nums[i - k]
            winSum -= outgoing

            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]

            incoming = nums[i]
            winSum += incoming
            freq[incoming] = freq.get(incoming, 0) + 1

            if len(freq) == k:
                maxSum = max(maxSum, winSum)
        return maxSum