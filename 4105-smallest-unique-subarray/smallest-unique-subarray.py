class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        nm = [nums]
        for k in range(n.bit_length() - 1):
            mp = {}
            nm.append([mp.setdefault(pair, len(mp)) for pair in zip(nm[k], nm[k][2 ** k:])])

        def found(length):
            k = length.bit_length() - 1
            return 1 in Counter(zip(nm[k], nm[k][length - 2 ** k:])).values()

        return bisect_left(range(1, n), True, key=found) + 1