class Solution:

  def minOperations(self, nums: list[int], x: int, k: int) -> int:
    n = len(nums)
    m = x // 2

    left = SortedList()
    right = SortedList()
    sum_left = 0
    sum_right = 0

    def balance():
      nonlocal sum_left, sum_right
      while len(left) > m:
        val = left.pop()
        sum_left -= val
        right.add(val)
        sum_right += val
      while len(right) > (x - m):
        val = right.pop(0)
        sum_right -= val
        left.add(val)
        sum_left += val

    def add(val: int):
      nonlocal sum_left, sum_right
      if right and val >= right[0]:
        right.add(val)
        sum_right += val
      else:
        left.add(val)
        sum_left += val
      balance()

    def remove(val: int):
      nonlocal sum_left, sum_right
      if right and val >= right[0]:
        right.remove(val)
        sum_right -= val
      else:
        left.remove(val)
        sum_left -= val
      balance()

    def get_cost():
      median = right[0]
      return sum_right - sum_left + (len(left) - len(right)) * median

    for i in range(x):
      add(nums[i])

    costs = [0] * (n - x + 1)
    costs[0] = get_cost()

    for i in range(1, n - x + 1):
      remove(nums[i - 1])
      add(nums[i + x - 1])
      costs[i] = get_cost()

    dp = [0] * (n + 1)
    inf = float("inf")

    for j in range(1, k + 1):
      next_dp = [inf] * (n + 1)
      for i in range(j * x, n + 1):
        next_dp[i] = min(next_dp[i - 1], dp[i - x] + costs[i - x])
      dp = next_dp

    return dp[n]