from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []
        for right in range(len(nums)):
            while dq and dq[0] <= right - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            if right >= k - 1:
                res.append(nums[dq[0]])
        return res