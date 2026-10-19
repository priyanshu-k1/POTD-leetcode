class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        start = 0
        count = 0

        for i in nums:
            if i < target:
                start += 1
            elif i == target:
                count += 1
        return [x for x in range(start,start+count)]

         