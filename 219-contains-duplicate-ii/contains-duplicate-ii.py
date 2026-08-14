class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = {}
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]] = i
            else:
                if abs(counter[nums[i]] - i) <= k:
                    return True
                else:
                    counter[nums[i]] = i
        return False
        