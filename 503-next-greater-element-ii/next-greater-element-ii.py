class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stk = []
        res = [-1] * n
        for i in range(2 * n - 1, -1, -1):
            idx = i % n
            while stk and stk[-1] <= nums[idx]:
                stk.pop()
            if stk:
                res[idx] = stk[-1]
            stk.append(nums[idx])
        return res